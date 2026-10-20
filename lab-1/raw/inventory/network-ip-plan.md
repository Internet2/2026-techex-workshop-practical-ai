# Katabatic Station IP plan

Last updated 2025-12-02 (Theo Nakamura). Domain: `kat.sprc.example`.

| Network | Range | VLAN | Purpose |
|---|---|---|---|
| Station LAN | 192.0.2.0/24 | 10 | Crew devices, printers, `kat-crew` Wi-Fi |
| Science | 198.51.100.0/24 | 20 | Instruments, science workstations, `kat-science` Wi-Fi |
| Management | 203.0.113.0/24 | 99 | Hypervisor, NAS, switch, UPS, modems |

## Fixed addresses (management VLAN)

| Host | Address | Notes |
|---|---|---|
| `sw-core-1` | 203.0.113.1 | Default gateway for all VLANs |
| `aurora` | 203.0.113.10 | Hypervisor |
| `ldap-01` | 203.0.113.11 | VM on aurora |
| `dns-01` | 203.0.113.12 | VM on aurora. Also DHCP. |
| `wiki-01` | 203.0.113.13 | VM on aurora |
| `tickets-01` | 203.0.113.14 | VM on aurora. `tickets.kat.sprc.example` |
| `snowdrift-01` | 203.0.113.15 | VM on aurora. Crew file share. |
| `icebox` | 203.0.113.20 | NAS |
| `penguin` | 203.0.113.21 | Backup NAS, Science building |
| `ups-comms-1` | 203.0.113.30 | UPS network card. Static. Re-set after firmware updates. |
| VSAT-1 modem | 203.0.113.40 | PolarLink managed |
| LEO puck | 203.0.113.41 | |
| `wap-01` to `wap-06` | 203.0.113.51 to .56 | |

## Printers (station LAN)

| Host | Address |
|---|---|
| `bergy` | 192.0.2.201 |
| `growler` | 192.0.2.202 |

## Wi-Fi

- `kat-crew`: WPA2-PSK, PSK rotates each season (laminated card in galley, and
  in the Handbook).
- `kat-science`: WPA2-Enterprise, certificates issued from `ldap-01`. Hanna's
  team gets these on request.
