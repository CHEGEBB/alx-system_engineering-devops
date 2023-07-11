# This script prints all possible combinations of two letters, except oo



# Type the following in the in the command line.
#!/bin/bash
echo {a..z}{a..z} | tr ' ' '\n' | grep -v "oo"
