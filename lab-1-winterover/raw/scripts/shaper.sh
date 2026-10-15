#!/bin/bash
# shaper.sh up|down
#
# Outbound rate cap on aurora's uplink-facing interface. The normal cap is
# 2 Mbit/s so that one person's upload cannot take the whole satellite link.
# "up" lifts it to 20 Mbit/s for the bulk-sync window; cron puts it back
# with "down". See the it user's crontab for the times.
#
# sreyes 2023-06. Interface name changed after the aurora rebuild, ihalvorsen 2024-10.

IFACE=ens19

case "$1" in
  up)   tc qdisc replace dev "$IFACE" root tbf rate 20mbit burst 256kbit latency 400ms ;;
  down) tc qdisc replace dev "$IFACE" root tbf rate 2mbit  burst 32kbit  latency 400ms ;;
  *)    echo "usage: $0 up|down" >&2; exit 2 ;;
esac

logger -t shaper "shaper $1 on $IFACE"
