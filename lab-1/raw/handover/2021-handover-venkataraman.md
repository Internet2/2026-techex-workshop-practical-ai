# IT Handover: Winter 2021

**From:** Priya Venkataraman (winterover IT 2021)
**To:** Marcus Lindqvist (winterover IT 2022)
**Written:** 2022-02-09, three days before the flight. Sorry for the typos.

Welcome to Katabatic. You are the IT department. You are also, when Bjorn is
asleep, the power department, and when Mei is on the roof, the comms department.
Nobody will tell you this in teh job description.

## The short version

- There are about 40 of us for 8 months. Everyone will know your name by week two
  and your Wi-Fi password opinions by week three.
- The internet is a geostationary VSAT link that we are too far south to point at
  comfortably. It works in windows. The windows are on a schedule Rosalind keeps.
  Do not promise anyone a video call.
- Everything important runs on one hypervisor called `aurora`. Treat it gently.
- Dana (2020) named everything after ice. `bergy` and `growler` are printers.
  `icebox` is the NAS. I did not change this and neither should you; the crew
  likes it.

## Systems as of Feb 2022

| Thing | What it is | Notes |
|---|---|---|
| `aurora` | Hypervisor, 2U, in the comms room rack | Runs DNS/DHCP, LDAP, the wiki, the ticket tracker, and `snowdrift` (file share) as VMs |
| `icebox` | 4-bay NAS, RAID-5 | Science data staging + crew share. Nightly sync to `penguin` |
| `penguin` | 2-bay NAS in the Science building | Backup target. It is in a different building on purpose (fire). |
| `sw-core-1` | Core switch, comms room | Everything hangs off it. Spare is in the cage, still boxed. |
| `bergy`, `growler` | Printers, galley corridor and Science | `bergy` jams when it is very cold outside. The paper dries out. Keep a ream in the sauna anteroom (not a joke; it works). |
| VSAT-1 | Primary dish, on the comms building roof | PolarLink. 20 down / 5 up when it is happy. |
| VSAT-2 | Backup dish, on the pad 80 m east | Smaller. Use it when VSAT-1 ices. |

## Things I wish someone had told me

1. **Generators.** Bjorn rotates duty generator A/B every 250 run-hours. You will
   be asked to help. The procedure is on the wall of the power room. Someone
   should type it up. The UPS in the comms rack carries `aurora` and the switch
   for about 30 minutes, which is plenty for a transfer, but if a transfer goes
   wrong, shut `aurora` down cleanly rather than ride it out.
2. **Skuas.** The large brown birds. One took a USB stick out of my jacket pocket
   on the walk to Science in March. It was the only copy of the March met data
   export. Jonah has not let me forget it. Put nothing you love in an open pocket.
3. **The sauna rule.** Friday 19:00 to 21:00 is sauna. There is no IT on Fridays
   19:00 to 21:00 unless the building is on fire. Rosalind enforces this and she
   is right.
4. **The crew share fills up.** `snowdrift` fills with movies by June. Quota it
   early, or make peice with it.
6. **Katabatic.** The wind that falls off the plateau, hence the station's name.
   Above about 50 kt it moves the big dish. You will hear the word daily.
5. **Tickets.** Make people file tickets. If you fix things from hallway
   conversations you will have no record and no sleep. Tracker is at
   `tickets.kat.sprc.example`, numbering is `KAT-NNNN`.

## Open items I am leaving you

- The spare `sw-core-1` has never been powered on. Please burn it in.
- `penguin` is on the Science building's circuit, which goes away first in a
  load shed. Ask Bjorn about moving it.
- Nobody knows what the breaker labels in panel P2 mean. Dana relabeled some of
  them in 2020. Whoever comes after you should fix this properly.

Good luck. It is a strange and wonderful place. You will miss it.

Priya
