This is a script that lists all the files with a .gif extension in the current directory and all its sub-directories.

Usage:

Open a text editor and create a new file.
Copy the following code into the file:
#!/bin/bash
find -type f -name "*.gif" | rev | cut -d "/" -f 1 | cut -d '.' -f 2- | rev | LC_ALL=C sort -f
