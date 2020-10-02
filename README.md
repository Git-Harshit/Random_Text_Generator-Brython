# Random Text Generator using Brython

This program generates a random (usually non-readable, meaningless) text for ***n*** number of paragraphs where ***n*** is taken as the user's input. It is capped to generate 100 paragraphs at random, which in return, increase the performance significantly. 

#### 🚀 Check out [here](https://git-harshit.github.io/Random_Text_Generator-Brython/).

## Table of Contents

- [About](#about)
- [Installation](#using-the-code)
- [Technology Stack](#technology-stack)
- [Contributing Here](#contributing-here)

## 📌 About

This program executes Python script(s) in website (with the help of Brython). It means that the Random Text is generated with a simple Python script (also using random module to ensure fresh, distinguished and unidentical result on every load), and the generated content is loaded on webpage using Brython.

### Installation

The code output for the latest release of the code in the master branch of this repository is also accessible at [Github Pages](https://git-harshit.github.io/Random_Text_Generator-Brython/).

To launch the code in local machine, [index.html](./index.html) file can be opened. 
However, the brython file may not get executed successfully on directly opening the index file from the repository source folder (with `IOError: can't load external script ... (AJAX calls not supported with protocol file:///` ).
Assuming that Python (Python v3, specifically) is already configured on your system, the code can be executed through localhost. One simple way to setup a localhost would be using the following one-liner in command terminal/window:

```python -m http.server [port]```

where using a custom port number is optional, as port number defaults to 8000 with `http.server` Python 3. More about it can be [read here](https://docs.python.org/3/library/http.server.html).
For Python 2, [SimpleHTTPServer](https://docs.python.org/2/library/simplehttpserver.html) can be used instead.

### Technology Stack

### Contributing Here

Contributions for this repository are welcome. If you can add anything for the betterment of this repository and any of its content(s), get started by reading the [contributing](./Contributing.md) file. Every change counts!
