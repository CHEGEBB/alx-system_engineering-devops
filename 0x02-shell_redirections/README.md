This is a script to Display the number of lines that contain the pattern “bin” in the file /etc/passwd

Usage:

Open a text editor and create a new file.
Copy the following code into the file:
#!/bin/bash
grep -c -i "bin" /etc/passwd
