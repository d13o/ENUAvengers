# ENUAvengers -- A Community Driven Enumivo Testnet

ENUAvengers is an Enumivo Testnet.

| Hero        | Producer Name           | Status  |
| ------------- |:-------------:| -----:|
|Stan Lee|stanlee|Claimed|
|Iron Man|ironman|Claimed|
|Captain America|captamerica|Claimed|
|Thor|thor|Claimed|
|Doctor Strange|drstrange|Available|
|Spider Man|spiderman|Available|
|Ant Man|antman|Available|
|Black Widow|blackwidow|Available|
|Hulk|hulk|Claimed|
|Hawk Eye|hawkeye|Available|
|Quick Silver|quicksilver|Available|
|Vision|vision|Claimed|
|War Machine|warmachine|Available|
|Falcon|falcon|Available|
|Black Panther|blackpanther|Available|
|Star Lord|starlord|Available|
|Captain Marvel|captmarvel|Available|
|Loki|loki|Claimed|
|Thanos|thanos|Available|
|Gamora|gamora|Available|
|Groot|groot|Available|

## Node Setup Guidance
### Build & install node components
make sure your repository is on the newest commit of [enumivo branch](https://github.com/enumivo/enumivo.git), then build and install.

```
git clone https://github.com/enumivo/enumivo.git
cd enumivo
git fetch origin enumivo
git checkout -b enumivo origin/enumivo
git submodule update --init --recursive
./enumivo_build.sh
cd build
make install
```
### Register your node information, and apply node account/keys
1. Domain name or IP address
1. http port for monitor RPC access (default: 8888)
1. P2P port (default: 9876)
1. Host location
1. Organization name (the organization name displayed in monitor page)

### Fetch ENUAvengers public configurations

```
git clone https://github.com/d13o/ENUAvengers.git
```
### Make your own node data directory, copy the configurations and scripts
```
mkdir <YOUR_DATA_DIR_PATH>
cd <ENUAvengers_REPO_PATH>
cp genesis.json config.ini start.sh stop.sh <YOUR_DATA_DIR_PATH>
```
### Fill in your node information
- Replace DATADIR in scripts start.sh stop.sh with <YOUR_DATA_DIR_PATH> 
- Fill in your node information and keys into config.ini

### Run enunode, check whether it works by watching the log file

```
cd <YOUR_DATA_DIR_PATH>
./start.sh
tail -f stderr.txt
```
### Produce the blocks
If enunode works well, please contact the administrator to grant your the privilege of producing blocks.


## Monitor Website
http://avengers-monitor.enuism.com

