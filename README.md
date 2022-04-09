# UoE Learn Login
A basic python program to log into the UoE MyEd page.


## Table of contents
1.  [Prerequisites](#prerequisites)
2.  [Installation](#installation)
3.  [Usage and Installation:](#usage) 
    
    3a. [Creating an executable (MacOS)](#execMacOS)
    
    3b. [Creating an executable using pyinstaller (All)](#execAll)

<a name="prerequisites"/></a>
## Prerequisites
* Selenium: 
```bash 
pip3 install -U selenium
```
* Webdriver_manager: 
```bash 
pip3 install -U webdriver_manager
```

* Keyring:
```bash
pip3 install -U keyring
```

* Pyinstaller (Optional):
```
pip3 install -U pyinstaller
```

Note:
Pyinstaller must be added to the PATH system environment variable

<a name="installation"/></a>
## Installation

Clone the repo

```bash
  git clone https://github.com/H00pyFr00d/edinburgh-uni-learn-login.git
```

Now, create `userinfo.txt` in the folder you've just created and store your username as follows:

```bash
  s2000000
```

<a name="usage"/></a>
## Usage and Installation

```bash
 python3 /Users/.../edinburgh-uni-learn-login/main.py
```

Will prompt the user for their username if they have not already created the `userinfo.txt` file, and their password if it hasn't already been provided

<a name="execMacOS"/></a>
### Creating an executable (MacOS)
In your desktop, create an `.exec` file:

```bash
 #!/bin/sh
 python3 /Users/.../edinburgh-uni-learn-login/main.py
 exit 0
```

Then give it permission,

```bash
 chmod +x /Users/.../open_learn.exec
```

#### Notes
1. When running the executable you might get an `operation not found` error, this could mean that your file's been [quarantined](https://www.alansiu.net/2021/08/19/troubleshooting-zsh-operation-not-permitted/).

2. If your shell window stays open after the script's finished running, go to **Terminal** > **Preferences** > **Profiles** > **Shell** and change the default setting for when the shell exists from "don't close the window" to "close the window"

<a name="execAll"/></a>
### Creating an executable using pyinstaller (All)
Install pyinstaller (as seen above)

Open a terminal instance and navigate to the `edinburgh-uni-learn-login` folder

Run the following command:
```bash
 pyinstaller main.py --onefile
```

Your executable will be placed in the folder you've run this command from
