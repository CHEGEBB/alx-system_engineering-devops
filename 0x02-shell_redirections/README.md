This is a script that decodes acrostics that use the first letter of each line

Usage:

Open a text editor and create a new file.
Copy the following code into the file:
#!/bin/bash
cut -c 1 | paste -s -d ''
