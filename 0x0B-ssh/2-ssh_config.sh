#!/usr/bin/env bash
# The script should configure the ssh client so that you can connect to 473254-web-01 using the private key ~/.ssh/school
Host 473254-web-01
    HostName 54.236.17.26
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
