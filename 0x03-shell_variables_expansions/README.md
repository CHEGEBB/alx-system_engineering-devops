# This script counts the number of directories in the PATH.



# Type the following in the in the command line.
#!/bin/bash
echo $PATH | tr -s ':' '\n' | wc -l