This script lists all files and directories in the current directory, separated by commas (,). It also adds a trailing slash to directory names and sorts the list alphabetically, with the directories . and .. listed at the very beginning.

To use the script, run it from the command line with the following command :
ls -ap | awk '{printf "%s, ", $0}' | sed 's/,\s$/\n/'