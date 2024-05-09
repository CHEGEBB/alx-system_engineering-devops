# 0x16. API advanced: Reddit API Project

This project aims to develop Python scripts that interact with the Reddit API to perform various tasks such as retrieving the number of subscribers for a subreddit, fetching the titles of hot posts, recursively fetching all hot articles, and counting the occurrences of specified keywords in hot post titles.

## Table of Contents

1. [Requirements](#requirements)
2. [Tasks](#tasks)
    - [Task 0: How many subs?](#task-0-how-many-subs)
    - [Task 1: Top Ten](#task-1-top-ten)
    - [Task 2: Recurse it!](#task-2-recurse-it)
    - [Task 3: Count it!](#task-3-count-it)
3. [Usage](#usage)
4. [Contributing](#contributing)
5. [Authors](#authors)

## Requirements <a name="requirements"></a>

- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Libraries imported in Python files must be organized in alphabetical order
- A `README.md` file, at the root of the folder of the project, is mandatory
- Code should use the PEP 8 style
- All files must be executable
- The length of the files will be tested using `wc`
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- The Requests module must be used for sending HTTP requests to the Reddit API

## Tasks <a name="tasks"></a>

### Task 0: How many subs? <a name="task-0-how-many-subs"></a>

Write a function `number_of_subscribers(subreddit)` that queries the Reddit API and returns the number of subscribers for a given subreddit. If the subreddit is invalid, return 0.

### Task 1: Top Ten <a name="task-1-top-ten"></a>

Write a function `top_ten(subreddit)` that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

### Task 2: Recurse it! <a name="task-2-recurse-it"></a>

Write a recursive function `recurse(subreddit, hot_list=[])` that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.

### Task 3: Count it! <a name="task-3-count-it"></a>

Write a recursive function `count_words(subreddit, word_list)` that queries the Reddit API, parses the titles of all hot articles, and prints a sorted count of given keywords.

## Usage <a name="usage"></a>

1. Clone the repository:

```bash
git clone https://github.com/waltertaya/alx-system_engineering-devops.git
```

2. Navigate to the appropriate directory for the task you want to execute (e.g., `0x16-api_advanced`).

3. Execute the Python script associated with the task you want to run.

```bash
python3 0-main.py programming
```

Replace `0-main.py` with the appropriate script and `programming` with the subreddit you want to query.

## Contributing <a name="contributing"></a>

Contributions are welcome! Feel free to submit pull requests or open issues if you find any bugs or have suggestions for improvement.

## Authors <a name="authors"></a>

Project created by ALX and done by waltertaya.
