This is a script that displays all users and their home directories, sorted by users

Usage:

Open a text editor and create a new file.
Copy the following code into the file:
#!/bin/bash
cut -d ':' -f 1,6 /etc/passwd | sort
