#!/usr/bin/env python3
"""nightly.py: Katabatic Station IT nightly digest.

Runs from cron on aurora at 03:30 station time (see the it user's crontab).
Collects a few health facts and posts one line to #comms-it so the
winterover sees them with the morning coffee.

Checks, in order:
  1. icebox (NAS): which bays are online, and SMART overall health per bay.
  2. ups-comms-1: battery charge and estimated runtime, over SNMP.
  3. Ticket tracker: anything past its due date.
  4. Inventory cross-check (unfinished).

History:
  2023-05  sreyes      first version (NAS + UPS)
  2024-03  ihalvorsen  overdue tickets, chat webhook
  2025-08  tnakamura   --quiet-fridays, started the inventory cross-check
  2026-02  tnakamura   handed over with the cross-check still a stub

"""

import argparse
import csv
import datetime as dt
import json
import logging
import subprocess
import sys
import urllib.request

NAS_HOST = "icebox.kat.sprc.example"
NAS_BAYS = 4
UPS_HOST = "203.0.113.30"
UPS_COMMUNITY = "public"            # TODO(sreyes 2023): change this. TODO(tnakamura 2025): still public.
UPS_OID_CHARGE = ".1.3.6.1.2.1.33.1.2.4.0"   # upsEstimatedChargeRemaining
UPS_OID_RUNTIME = ".1.3.6.1.2.1.33.1.2.3.0"  # upsEstimatedMinutesRemaining
TICKETS_API = "https://tickets.kat.sprc.example/api/tickets?state=open"
CHAT_WEBHOOK = "https://wiki-01.kat.sprc.example/hooks/comms-it"
INVENTORY_CSV = "/srv/it-docs/inventory/hardware-inventory.csv"

# Nobody gets paged during sauna. This also suppresses the chat post, which
# in hindsight means Friday problems are reported on Saturday. Known.
SAUNA = {"weekday": 4, "start": dt.time(19, 0), "end": dt.time(21, 0)}

log = logging.getLogger("nightly")


def ssh(host: str, *cmd: str) -> str:
    """Run a command on a host over SSH and return stdout."""
    out = subprocess.run(["ssh", "-o", "BatchMode=yes", host, *cmd],
                         capture_output=True, text=True, timeout=60, check=False)
    return out.stdout


def check_nas() -> dict:
    """Bays online and SMART overall-health per bay.

    TODO(tnakamura 2025-11): -H is coarse. Parse -A for Reallocated_Sector_Ct.
    """
    online, passed, serials = 0, 0, []
    for bay in range(1, NAS_BAYS + 1):
        dev = f"/dev/sd{chr(ord('a') + bay - 1)}"
        health = ssh(NAS_HOST, "sudo", "smartctl", "-H", "-i", dev)
        if not health.strip():
            continue
        online += 1
        if "PASSED" in health:
            passed += 1
        for line in health.splitlines():
            if line.startswith("Serial Number:"):
                serials.append(line.split(":", 1)[1].strip())
    return {"online": online, "passed": passed, "serials": serials}


def check_ups() -> dict:
    """Battery charge and estimated runtime from the UPS network card."""
    def snmp(oid: str) -> int:
        out = subprocess.run(["snmpget", "-v2c", "-c", UPS_COMMUNITY, "-Oqv", UPS_HOST, oid],
                             capture_output=True, text=True, timeout=20, check=False)
        return int(out.stdout.strip() or 0)
    return {"charge": snmp(UPS_OID_CHARGE), "runtime_min": snmp(UPS_OID_RUNTIME)}


def check_tickets() -> int:
    """Count open tickets whose due date is in the past."""
    with urllib.request.urlopen(TICKETS_API, timeout=20) as resp:
        tickets = json.load(resp)
    today = dt.date.today().isoformat()
    return sum(1 for t in tickets if t.get("due") and t["due"] < today)


def cross_check_inventory(serials: list[str]) -> list[str]:
    """Compare serials found in the array against the inventory CSV.

    Intended to flag any serial in the array that the inventory does not
    list in a bay. Started 2025-08. The CSV read works; the comparison is
    not written yet (the notes column is free text and I had not decided
    how to treat it). Left raising so the digest says "skipped" rather than
    pretending it ran.
    """
    with open(INVENTORY_CSV, newline="") as fh:
        rows = list(csv.DictReader(fh))
    log.debug("inventory rows: %d, serials in array: %s", len(rows), serials)
    raise NotImplementedError("inventory cross-check not finished (tnakamura)")


def in_sauna(now: dt.datetime) -> bool:
    return now.weekday() == SAUNA["weekday"] and SAUNA["start"] <= now.time() <= SAUNA["end"]


def post(text: str) -> None:
    body = json.dumps({"username": "nightly-bot", "text": text}).encode()
    req = urllib.request.Request(CHAT_WEBHOOK, data=body, headers={"Content-Type": "application/json"})
    urllib.request.urlopen(req, timeout=20)


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--quiet-fridays", action="store_true", help="do not post during the sauna window")
    ap.add_argument("--dry-run", action="store_true", help="print the digest instead of posting it")
    args = ap.parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    now = dt.datetime.now()
    if args.quiet_fridays and in_sauna(now):
        log.info("sauna window; not posting")
        return 0

    parts = [f"digest {now:%Y-%m-%d}"]

    nas = check_nas()
    parts.append(f"icebox: {nas['online']}/{NAS_BAYS} online, SMART PASSED x{nas['passed']}")

    ups = check_ups()
    parts.append(f"ups-comms-1: battery {ups['charge']}%, est. runtime {ups['runtime_min']} min")

    try:
        parts.append(f"tickets overdue: {check_tickets()}")
    except Exception as exc:  # tracker VM reboots at 03:00 on patch nights
        log.warning("ticket check failed: %s", exc)
        parts.append("tickets overdue: ?")

    try:
        bad = cross_check_inventory(nas["serials"])
        parts.append("inventory cross-check: " + (f"MISMATCH {bad}" if bad else "ok"))
    except NotImplementedError:
        parts.append("inventory cross-check: skipped (not implemented)")

    digest = " | ".join(parts)
    if args.dry_run:
        print(digest)
    else:
        post(digest)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
