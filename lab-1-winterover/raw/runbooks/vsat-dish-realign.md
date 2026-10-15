# Runbook: VSAT-1 realignment after a wind event

**Version 2, 2025-04-02.** Sam Reyes (v1 2023), updated Mei-Ling Tsai.

Katabatic winds above about 50 kt move the VSAT-1 dish by up to half a degree.
Symptoms: link drops to zero or a few hundred kbit/s, modem shows low Es/No,
PolarLink NOC may call before you notice.

## Before you go on the roof

- Two people, always. Harness clipped to the roof line.
- Wind below 25 kt and not forecast to rise. If it is still blowing, fail over
  to VSAT-2 (Failover section below) and wait.
- Radio check with the station manager.

## Procedure

1. On the modem console, note the current Es/No and the beacon receive level.
2. Loosen the azimuth and elevation locks on the mount (two 17 mm bolts each).
3. Peak on the beacon. Nominal pointing for VSAT-1 as of this version:
   **azimuth 357.4°, elevation 8.1°**. The beacon is on **12.199 GHz**
   (downlink). Expect a usable Es/No of 9 dB or better.
4. Lock the mount. Re-check Es/No after locking; it often drops when you
   tighten the bolts.
5. Call PolarLink NOC (number in the Handbook) and ask them to confirm carrier
   from their side.
6. Open a ticket tagged `vsat` with before/after Es/No.

## Failover to VSAT-2

VSAT-2 is the smaller dish on the pad 80 m east. Swap the modem's RF input at
the patch panel (clearly labelled, one of the few things that is). Expect about
a third of the normal bandwidth. Tell Mei; she needs to re-schedule the science
uplink windows.
