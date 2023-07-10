This is a script that parses web servers logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests.

Usage:

Open a text editor and create a new file.
Copy the following code into the file:
#!/bin/bash
tail -n +2 | cut -f -1 | sort -k 1 | uniq -c | sort -rnk 1 | head -n 11 | rev | cut -d ' ' -f -1 | rev
