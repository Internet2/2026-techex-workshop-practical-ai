# Runbook: Generator duty transfer (A/B rotation)

**Version 3, effective 2026-01-15.** Supersedes the 2022 procedure, which is kept
in `archive/` for history only. Applies to the two 350 kW gensets installed
during the 2025-26 summer.

**Owner:** Bjorn Haldane (facilities). IT winterover is the trained backup and
is responsible for the comms rack during any transfer.

## Policy

1. **Rotation interval: every 500 run-hours** of the duty generator, or sooner
   if facilities calls it. (The 2025 gensets have a 500 h service interval; the
   old 250 h figure applied to the retired units.)
2. **Pre-warm the standby for 20 minutes.** Block heater on, coolant at or above
   40 °C before the standby is started. Cold starts are the main cause of a
   failed transfer.
3. **Never transfer when the wind is above 40 kt.** Intake icing on the standby
   during a katabatic event caused the July 2024 blackout. Check the met screen
   in the power room; if in doubt, wait. The duty generator can run past 500 h
   without harm. A failed transfer in a storm cannot be undone.
4. Comms rack UPS (`ups-comms-1`) must show at least 80% charge before starting.

## Procedure

1. Confirm wind below 40 kt and forecast to stay there for an hour.
2. Confirm UPS at or above 80%. IT: stay in the comms room for the duration.
3. Block heater on standby for 20 min; confirm coolant temperature.
4. Start standby, let it reach rated speed, confirm voltage and frequency stable
   for 2 minutes on the panel.
5. Synchronise and close the standby breaker. Open the duty breaker.
6. Confirm load transferred, UPS back on mains, no alarms.
7. Run the old duty unit down per the manufacturer's cool-down timer, then stop.
8. Log run-hours for both units in the power-room logbook and in the ticket
   tracker (one ticket per transfer, tag `power`).

## If the transfer fails

- UPS runtime is about 25 minutes at current comms rack load.
- At **15 minutes on battery with no mains**, IT shuts down `aurora` cleanly
  (`snowdrift` first, then LDAP, then the hypervisor). Do not wait for Bjorn to
  tell you.
- Reopen the standby breaker, reclose duty, investigate the standby after power
  is stable.
