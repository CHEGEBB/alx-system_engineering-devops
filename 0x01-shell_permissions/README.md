#!/bin/bash

# Set permissions for the file hello
chmod 753 hello

# Print the new permissions
echo "The new permissions for the file hello are: $(stat -c "%a" hello)"

