#!/usr/bin/python
import subprocess
import json

BIN_DIR = '/usr/local/bin/'
WALLET_URL = 'http://127.0.0.1:8899'


def load_bps_config():
    with open('bp_keys.json', 'r') as f:
        r = f.read()
    configs = json.loads(r)
    config_dict = {}
    for name, priv_key, pub_key in configs:
        config_dict[name] = (priv_key, pub_key) 
    return config_dict


def create_account(name, owner_key, active_key):
    enucli = BIN_DIR + 'enucli'
    output = subprocess.check_output([enucli, "--wallet-url", WALLET_URL, "create", "account", "enumivo", name, owner_key, active_key])
    print output


if __name__ == '__main__':
    configs = load_bps_config()
    for name, keys in configs.iteritems():
        create_account(name, keys[1], keys[1])
