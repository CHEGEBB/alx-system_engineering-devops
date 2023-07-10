This is a script that counts the number of directories and sub-directories in the current directory.

Usage:

Open a text editor and create a new file.
Copy the following code into the file:
#!/bin/bash
find . -type d -not -name '.' | wc -l
