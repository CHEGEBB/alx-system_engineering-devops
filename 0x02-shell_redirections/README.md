This is a script that deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders.
Usage:

Open a text editor and create a new file.
Copy the following code into the file:
#!/bin/bash
find . -type f -name "*.js" -delete
