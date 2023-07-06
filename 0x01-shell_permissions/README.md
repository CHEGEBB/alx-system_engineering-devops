#!/bin/bash

# Get the current permissions for the file hello
permissions=$(stat -c "%a" hello)

# Add execute permission for the owner
new_permissions=$(echo "$permissions" | sed "s/^-rw-r--r--/-rwxr--r--/")

# Change the permissions of the file
chmod $new_permissions hello

# Print the new permissions
echo "The new permissions for the file hello are: $new_permissions"

