This is a script to Display all the lines in the file /etc/passwd that do not contain the pattern “bin”.

Usage:

Open a text editor and create a new file.
Copy the following code into the file:
#!/bin/bash
grep -i -v "bin" /etc/passwd
