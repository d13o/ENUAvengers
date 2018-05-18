#!/bin/bash
BINDIR=/usr/local/bin
DATADIR=/root/mainnode

if [ "$1" = "bootstrap" ]
then
OPT="--enable-stale-production"
fi

$BINDIR/enunode $OPT --data-dir $DATADIR --config-dir $DATADIR > $DATADIR/stdout.txt 2> $DATADIR/stderr.txt & echo $! > $DATADIR/eosd.pid
