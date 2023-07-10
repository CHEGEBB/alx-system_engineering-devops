This is a command that finds all empty files and directories in the current directory and all sub-directories

Usage:

Open a text editor and create a new file.
Copy the following code into the file:
#!/bin/bash
find . -empty | rev | cut -d '/' -f 1 | rev