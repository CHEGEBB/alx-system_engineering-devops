This is a script that displays the 10 newest files in the current directory

Usage:

Open a text editor and create a new file.
Copy the following code into the file:
#!/bin/bash
ls -t1 | head -n 10
