# Runbook: Power room and comms rack UPS

**Version 2, 2023-11-04.** Sam Reyes. Minor edits Theo Nakamura 2025-06.

## Where things are

- Power room is the first door on the left past the galley, before the boot room.
- Panel **P1**: generator output and building mains. Do not touch. Facilities only.
- Panel **P2**: sub-distribution for the comms building side. This is the panel
  IT may need.
- Comms rack UPS `ups-comms-1` is at the bottom of the rack. It feeds `aurora`,
  `icebox`, `sw-core-1`, and the VSAT-1 modem. It does **not** feed `penguin`
  (different building) or the printers.

## Hard power-cycle of the comms rack UPS

Use only if the UPS is hung and will not respond on its console or network
card. Everything behind it goes dark; shut `aurora` down cleanly first if you
possibly can.

1. Shut down `aurora` VMs, then the hypervisor. Shut down `icebox`.
2. In panel P2, open the breaker labelled **`IT-UPS`**.
3. Wait 30 seconds. Hold the UPS power button for 5 seconds to drain the logic
   board.
4. Close `IT-UPS`. The UPS self-tests for about a minute and then restores output.
5. Power on `sw-core-1`, then `icebox`, then `aurora`. Check the VMs came up.

## Known issues

- P2 labels were partly rewritten in 2020 and may not all be accurate. The
  `IT-UPS` label is believed correct but has not been traced end to end.
- The UPS network card loses its IP after a firmware update. Static config is in
  `inventory/network-ip-plan.md`.
