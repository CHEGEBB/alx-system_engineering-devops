This is a script to Display lines containing the pattern “root” and 3 lines after them in the file /etc/passwd.

Usage:

Open a text editor and create a new file.
Copy the following code into the file:
#!/bin/bash
grep -i "root" -A 3 /etc/passwd
