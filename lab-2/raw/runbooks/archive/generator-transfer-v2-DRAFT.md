# Runbook: Generator duty transfer (A/B rotation)

**Version 2, DRAFT 2024-08-03. Not issued.** Ingrid Halvorsen, typing up
Bjorn's notes after the July blackout. Bjorn has not signed this off, and the
replacement gensets due on the 2025-26 resupply will change the numbers again,
so this may never be issued. Kept so the wind rule is written down somewhere.

## Policy

- Rotate the duty generator **every 250 run-hours** (unchanged from v1).
- **NEW: do not transfer when the wind is above 40 kt.** Intake icing stalled
  Gen B during the 2024-07 transfer at 45 kt. Thirty-one minutes on UPS.
- **NEW: comms rack UPS at or above 80% before starting.**
- Either unit may be the duty unit. Alternate.

## Procedure

1. Check the met screen. Above 40 kt, stop here and wait.
2. Start the standby generator.
3. Wait for voltage to stabilise (about 2 minutes).
4. Close the standby breaker, open the duty breaker.
5. Confirm load transferred and the comms UPS is back on mains.
6. Stop the old duty unit after its cool-down.
7. Write the run-hours in the power room logbook.

## Open questions for Bjorn

- Pre-warm? You said "the new ones will need it". How long?
- Does IT shut `aurora` down at a fixed minute on battery, or on your call?
  July we had no rule and lost the LDAP VM.
