This is a script to Display all lines of the file /etc/ssh/sshd_config starting with a letter.

Usage:

Open a text editor and create a new file.
Copy the following code into the file:
#!/bin/bash
grep -i "^[a-z]" /etc/ssh/sshd_config
