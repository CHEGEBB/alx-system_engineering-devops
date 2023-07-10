This is a simple shell script that uses the echo command to script that displays the third line of the file iacta

Usage:

Open a text editor and create a new file.
Copy the following code into the file:
#!/bin/bash
head -n 3 iacta | tail -n +3
