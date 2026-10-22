# Runbook: Accounts for new arrivals

**Version 4, 2026-02-10.** Theo Nakamura.

Do this for every person on the arrival manifest **before** the flight lands.
They will be tired, cold, and want to message home. Having their account ready
is the best first impression IT can make.

1. Get the manifest from the station manager.
2. Create the LDAP account on `aurora` (`ldap-01` VM): username is first
   initial + surname, lower case. Add to group `crew`. Science staff also go in
   `science`.
3. Set the initial password to the pattern in the sealed envelope in the comms
   room safe. Force change at first login.
4. Create their `snowdrift` home with the default 50 GB quota. Exemptions need
   the station manager's say-so (currently: the chef).
5. Add them to the ticket tracker.
6. Crew Wi-Fi (`kat-crew`) PSK rotates each season; the current one is on the
   laminated card in the galley and in the Handbook. Science devices go on
   `kat-science` (certificate, see IP plan).
7. Personal internet allowance is set per person in the comms sheet, not by IT.
   Point them at the sheet. Do not negotiate allowances; that is Mei and
   Rosalind.
8. Day one: walk them through the Handbook's acceptable-use section.
