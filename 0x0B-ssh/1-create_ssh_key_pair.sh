#!/usr/bin/env bash
# This script creates an RSA key pair.
# The public key is saved in the file ~/.ssh/holberton
# The private key is saved in the file ~/.ssh/holberton
# The key pair should have a passphrase
# The key pair should have the default comment
# The script should return 0

# Create a new RSA key pair
ssh-keygen -t rsa -b 4096 -C "Holberton" -f ~/.ssh/holberton -N ""
exit 0
