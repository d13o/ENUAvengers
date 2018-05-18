#!/usr/bin/python
import subprocess
import json

BIN_DIR='/usr/local/bin/'

BP_NAMES = [
    'Thanos',
    'CaptainAmerica',
    'IronMan',
    'Thor',
]


def create_key():
    enucli = BIN_DIR + 'enucli'
    output = subprocess.check_output([enucli, "create", "key"])
    _, _, priv_key, _, _, pub_key = output.split()
    return priv_key, pub_key


def gen_bp_keys():
    output = []
    for n in BP_NAMES:
        priv_key, pub_key = create_key()
        output.append([n, priv_key, pub_key])
    return output


def gen_setprods(bp_keys):
    output = {"version": "123456", "producers": []}
    for name, priv_key, pub_key in bp_keys:
        output["producers"].append({"producer_name": name, "block_signing_key": pub_key})
    return output


if __name__ == '__main__':
    bp_keys = gen_bp_keys()
    bp_keys_json = json.dumps(bp_keys, indent=4)
    setprods_json = json.dumps(gen_setprods(bp_keys), indent=4)

    print 'write bp_keys to file bp_keys.json'
    with open('bp_keys.json', 'w') as f:
        f.write(bp_keys_json)

    print 'write setprods to file setprods.json'
    with open('setprods.json', 'w') as f:
        f.write(setprods_json)

    print 'all done'
