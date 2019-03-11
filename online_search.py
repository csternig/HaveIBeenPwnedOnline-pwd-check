#!/usr/bin/python3
# -*- coding: utf-8 -*-
import getpass
import hashlib
import requests

if __name__ == "__main__":
    while True:
        test_password = getpass.getpass('Enter password:')
        if not test_password:
            break
        test_hash = hashlib.sha1(test_password.encode()).hexdigest().upper()
        test_prefix = test_hash[:5]
        print("Transmit hashed value over Internet: {}".format(test_prefix))
        result = requests.get('https://api.pwnedpasswords.com/range/{}'.format(test_prefix))
        num_hits = 0
        for line in result.text.split('\r\n'):
            partial_hash, count = line.split(':')
            if test_hash[5:] == partial_hash:
                num_hits = count
                break
        print("The password has been found {} times".format(num_hits))
