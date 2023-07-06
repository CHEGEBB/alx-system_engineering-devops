#!/bin/bash

# Use chmod to change the permissions of the file hello
chmod ugo+x hello

# Print the new permissions
echo "The new permissions for the file hello are: $(stat -c "%a" hello)"

