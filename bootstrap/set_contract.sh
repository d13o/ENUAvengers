#!/bin/bash

BINDIR=/usr/local/bin
WALLETURL="http://127.0.0.1:8899"
BIOSPATH="/root/enumivo/build/contracts/enumivo.bios"

$BINDIR/enucli --wallet-url $WALLETURL set contract enumivo $BIOSPATH
