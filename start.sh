#!/bin/bash
BINDIR=/usr/local/bin
DATADIR=/root/mainnode

$BINDIR/enunode --enable-stale-production --data-dir $DATADIR --config-dir $DATADIR > $DATADIR/stdout.txt 2> $DATADIR/stderr.txt & echo $! > $DATADIR/eosd.pid
