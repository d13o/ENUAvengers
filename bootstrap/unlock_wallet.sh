#!/bin/bash

BINDIR=/usr/local/bin
WALLETURL="http://127.0.0.1:8899"

$BINDIR/enucli --wallet-url $WALLETURL wallet unlock
