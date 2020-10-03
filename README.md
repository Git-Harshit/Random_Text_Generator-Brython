# Random Text Generator using Brython

[![GitHub issues](https://img.shields.io/github/issues/Git-Harshit/Random_Text_Generator-Brython?style=for-the-badge)](https://github.com/Git-Harshit/Random_Text_Generator-Brython/issues)
![GitHub repo size](https://img.shields.io/github/repo-size/Git-Harshit/Random_Text_Generator-Brython?style=for-the-badge)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Git-Harshit/Random_Text_Generator-Brython?style=for-the-badge)
[![GitHub license](https://img.shields.io/github/license/Git-Harshit/Random_Text_Generator-Brython?style=for-the-badge)](https://github.com/Git-Harshit/Random_Text_Generator-Brython/blob/master/LICENSE)
[![Website](https://img.shields.io/website?style=for-the-badge&url=https%3A%2F%2Fgit-harshit.github.io%2FRandom_Text_Generator-Brython%2F)](https://git-harshit.github.io/Random_Text_Generator-Brython/)
![GitHub Hacktoberfest combined status](https://img.shields.io/github/hacktoberfest/2020/Git-Harshit/Random_Text_Generator-Brython?style=for-the-badge)

This program generates a random (usually non-readable, meaningless) text for ***n*** number of paragraphs where ***n*** is taken as the user's input. It is capped to generate 1-100 random paragraphs, so as to keep the performance significant. 

#### 🚀 Check out the live tool [here](https://git-harshit.github.io/Random_Text_Generator-Brython/).

## Table of Contents

- [About](#about)
- [Usage](#usage)
- [Technology Stack](#technology-stack)
- [Contributing](#contributing)

## About 

This program executes Browser Python [(Brython)](https://brython.info/). Wait, what? What do you mean by “Browser Python”? <br />
It means that the Random Text is generated with a simple Python script (also using random module to ensure fresh, distinguished and unidentical result on every load), and the generated content is loaded on webpage using Brython.

## Usage 

#### Requirement - [Python 3x](https://www.python.org/downloads/) should be installed, for running localhost

The code can be run through localhost. Assuming that Python (Python v3, specifically) is already configured on your system, one simple way to setup a localhost would be by using the Command Line/Command Prompt in the same directory, and entering:

```
python -m http.server [port]
``` 

where using a custom port number is optional, as port number defaults to 8000 with `http.server`. More about it can be [found here](https://docs.python.org/3/library/http.server.html).

▶ For Python 2 supported terminals, [SimpleHTTPServer](https://docs.python.org/2/library/simplehttpserver.html) can be used instead.

_Note_: To launch the code in local machine, [index.html](./index.html) file cannot be directly opened, as the brython file may not get executed successfully while opening the index file from the repository source folder (with "IOError: can't load external script ... (AJAX calls not supported with protocol file:///" ). So, localhost server setup is preferred.

## Technology Stack

The following tools and technology are currently in use here.

1. Brython
2. Python
3. HTML
4. CSS

## Contributing

Your contributions are always welcome! 😀 <br/>
Please take a look at our [contributing](./Contributing.md) guidelines if you're interested in helping towards making the repository better!

Every change counts! 🔄
