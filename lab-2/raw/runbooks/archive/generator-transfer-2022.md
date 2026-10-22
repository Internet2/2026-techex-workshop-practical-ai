# Runbook: Generator duty transfer (A/B rotation)

**Version 1, 2022-03-20.** Written by Marcus Lindqvist from Bjorn's wall notes.

## Policy

- Rotate the duty generator **every 250 run-hours**.
- Either unit may be the duty unit. Alternate.
- Transfers may be done at any time the standby starts cleanly.

## Procedure

1. Start the standby generator.
2. Wait for voltage to stabilise (about 2 minutes).
3. Close the standby breaker, open the duty breaker.
4. Confirm load transferred and the comms UPS is back on mains.
5. Stop the old duty unit after its cool-down.
6. Write the run-hours in the power room logbook.

## Notes

- The comms UPS carries the rack for roughly 30 minutes. A transfer takes under
  five. There is plenty of margin.
- If the standby will not start, do not keep cranking it. Call Bjorn.
