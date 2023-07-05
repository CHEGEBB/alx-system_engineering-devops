# HTML File Copy Script

This shell script allows you to copy HTML files from the current working directory to the parent directory, but only if the files do not already exist in the parent directory or if they are newer than the versions in the parent directory.

## Usage

1. Open a terminal or command prompt.

2. Navigate to the directory containing the HTML files you want to copy.

3. Run the following command:

find . -name "*.html" -newer -mtime 0 -exec cp {} ../ \;

