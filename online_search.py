#!/usr/bin/python3
# -*- coding: utf-8 -*-
import getpass
import hashlib
import requests

if __name__ == "__main__":
        print("Please enter a password for testing against the Have I Been Pawned database.")
        print("Use no password an just press ENTER to exit the program.\n")
        # reading a password from prompt in a secure way
        password_console = getpass.getpass('Enter password:')
        # creating a SHA1 hash of the password and reformat it for HIBP upload
        password_hash = hashlib.sha1(password_console.encode()).hexdigest().upper()
        print("Your local SHA1 password hash: {}".format(password_hash))
        # using only the first 5 digits of the password hash to query the Internet database
        password_prefix = password_hash[:5]
        print("Transmit hashed value over Internet: {}".format(password_prefix))
        # querying the results, a list of password SHA1 hash values
        result = requests.get('https://api.pwnedpasswords.com/range/{}'.format(password_prefix))
        num_hits = 0  # introducing a hit count variable
        for line in result.text.split('\r\n'):
            # Have i been pawned returns a partial password hash (all digits except the first 5 and a count value
            # separated by ':' for every possible hit
            partial_hash, count = line.split(':')  # type: (str, int)
            # check if tha password_hash (local value) matches the partial_hash (remote value from database)
            if password_hash[5:] == partial_hash:
                # if there's a match num_hits is updated with the count value and the for loop is left
                num_hits = count
                break
        print("The password has been found {} times".format(num_hits))
