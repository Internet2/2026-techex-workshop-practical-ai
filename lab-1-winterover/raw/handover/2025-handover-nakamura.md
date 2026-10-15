# IT Handover: Winter 2025

**From:** Theo Nakamura (winterover IT 2025)
**To:** it-winter (2026)
**Written:** 2026-02-12. We have overlapped for five days so far, so this is
the stuff I either forgot to say out loud or said while you were jet-lagged.

I tried to write the handover I wished I had received. It is long. Read the
"Do not" list first if you read nothing else.

## Do not

- **Do not use the drive in the antistatic bag on the shelf above the rack as a
  spare.** It is serial **WX-7702**, the drive that failed out of `icebox` bay 1
  in September 2024. It is on the shelf because the RMA needs the physical drive
  back and it has missed two resupply vessels. Ingrid wrote this down, I am
  writing it down again. The replacement spare Rosalind ordered was back-ordered
  and is now on the **October 2026 relief flight** manifest. Until then there is
  **no spare drive on station.** If `icebox` loses a disk, it runs degraded until
  October; do not "fix" it with the bag.
- **Do not transfer generators in wind above 40 kt.** This is now in the v3
  runbook (`runbooks/generator-transfer.md`, effective 2026-01-15). The old
  250-hour procedure is in `runbooks/archive/` for history. The new gensets
  rotate at **500 run-hours** and need a 20-minute pre-warm. Bjorn wrote v3, I
  typed it.
- **Do not trust the P2 breaker labels.** Sam's power-room runbook says the comms
  rack UPS is on `IT-UPS`. Bjorn insists it is not and that `IT-UPS` feeds
  something in the galley. I never had reason to flip either so I never
  confirmed it. Trace it with Bjorn before you ever need to.
- **Do not promise video calls.** Still true. The LEO puck helps but only in its
  windows.
- **Do not schedule anything Friday 19:00 to 21:00.** Sauna.

## Systems as of Feb 2026

Hardware list with serials is in `inventory/hardware-inventory.csv` (I updated it
in December). IP plan in `inventory/network-ip-plan.md`.

| Thing | State | Notes |
|---|---|---|
| `aurora` | Fine. Rebuilt LDAP VM (2024) is solid. | Snapshots nightly to `icebox`, weekly to `penguin`. |
| `icebox` | 4-bay RAID-5, all healthy as of Feb. | **No spare on station** (see above). Bay 3 (WX-7731) has shown a few reallocated sectors since November; watch it. |
| `penguin` | Fine. Still on the Science circuit. | Bjorn and I agreed it moves to the comms circuit in the 2026-27 summer. Not done. |
| `sw-core-1` | Fine. | **The spare has still never been powered on.** It has become a tradition. Break the tradition. |
| VSAT-1 / VSAT-2 | Fine. | Realign runbook is v2 (2025). PolarLink sent a contract notice in January that changes some numbers; it is in `vendors/`. I have not reconciled it with the runbook. |
| LEO puck | Works in its windows. | Mei owns it. Schedule is in the comms sheet. |
| `bergy`, `growler` | Fine. Paper in the sauna anteroom. | Luis moved the ream once. Chaos. |
| UPS `ups-comms-1` | Batteries replaced 2025-01. ~25 min runtime at current load. | |
| `nightly.py` on `aurora` | Runs 03:30 from cron, posts a digest to #comms-it. | `scripts/nightly.py`. Read it before you trust it; I added a fourth check in August and ran out of year. |

## Where the documentation is

Some of it is here on disk in this folder, which you are now the owner of. Some
of it is **not on disk and should not be**, because it changes weekly and other
people own it:

- **The Winter 2026 Station Handbook** (crew roles, comms policy, acceptable use,
  emergency numbers) is a Google Doc Rosalind maintains. Public, read-only.
- **The comms schedule** (satellite windows, LEO windows, bulk-sync slots,
  personal bandwidth allowance) is a Google Sheet Mei maintains. Also public and
  read-only, also changes weekly.
- **The all-hands kickoff slides** Rosalind presents on day one. Public.

Links for all three are in `comms/comms-schedule-pointer.md`. When someone asks
"when is the next bulk sync window" the answer is in the sheet, not in your head
and not in this folder. Do not copy the sheet into the repo. It will be wrong
within a week.

## People

- **Rosalind Achebe**, station manager. Owns the Handbook and the kickoff deck.
  Decisive, fair, enforces the sauna rule.
- **Bjorn Haldane**, facilities and power. Generators, breakers, heating. Knows
  where everything is. Will not write it down.
- **Mei-Ling Tsai**, comms tech. VSAT, LEO puck, HF radio. Shares the comms room
  with you. Excellent. Will help you with anything and you should help her with
  anything.
- **Luis Ferreira**, chef. Controls morale. Has a `snowdrift` quota exemption.
  Is protective of the galley walk-in freezer.
- **Jonah Pike**, met tech. Has video of everything.
- **Dr. Hanna Kowalczyk**, science lead. Her data is why we are here. Science
  VLAN requests come from her.
- **Dr. Omar Haddad**, medic. The only person allowed to override the sauna rule.

## Calendar

- 2026-02-14: last flight out (me, on it).
- 2026-10-28 (weather permitting): first relief flight in. Carries the `icebox`
  spare drive and the new winterover. **Your handover is due before it lands.**
- 2027-01: resupply vessel. The RMA drive finally leaves.

## Open items

1. Trace P2 with Bjorn.
2. Power on the spare `sw-core-1`.
3. Reconcile the PolarLink January notice with the VSAT runbook.
4. Move `penguin` (summer).
5. Watch `icebox` bay 3.

It was a good year. You will be fine. File tickets, even on yourself.

Theo
