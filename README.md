# Random Text Generator with Brython

Random Text Generator with Python and Brython script.

### Table of Contents
- [Main Heading](#Random-Text-Generator-with-Brython)
- [About Code](#About)
- [Using the Code](#using-the-code)

### About
This program executes Python script(s) in website (with the help of Brython). It means that the Random Text is generated with a simple Python script (also using random module to ensure fresh, non-consistent and unidentical result on every load), and the generated content is loaded on webpage using Brython.

### Using the code
The code output for the latest release of the code in the master branch of this repository is also accessible at [Github Pages](https://git-harshit.github.io/Random_Text_Generator-Brython/).

To launch the code in local machine, [index.html](./index.html) file can be opened. 
However, the brython file may not get executed successfully on directly opening the index file from the repository source folder `(with IOError: can't load external script ... (Ajax calls not supported with protocol file:///)`).
Assuming that Python (Python v3, specifically) is already configured on your system, the code can be executed through localhost. One simple way to setup a localhost would be using the following one-liner in command terminal/window:
```python -m http.server [port]```
where using a custom port is optional. More about it can be [read here](https://docs.python.org/3/library/http.server.html).
For Python 2, [SimpleHTTPServer](https://docs.python.org/2/library/simplehttpserver.html) can be used instead.
