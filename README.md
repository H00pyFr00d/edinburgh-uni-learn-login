# UoE Learn Login

A basic python program to log into the UoE learn page.

## Table of contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Usage](#usage)
   --> [Creating an executable (MacOS)](#execMacOS)

<a name="prerequisites"/></a>

## Prerequisites

* Selenium:

```bash 
pip install -U selenium
```

* Webdriver_manager:

```bash 
pip install -U webdriver_manager
```

<a name="installation"/></a>

## Installation

Clone the repo

```bash
  git clone https://github.com/H00pyFr00d/edinburgh-uni-learn-login.git
```

Now, create `userinfo.txt` in the folder you've just created and store your username and password as follows:

```bash
  s2000000
  $$£$£%£@$
```

<a name="usage"/></a>

## Usage

```bash
 python3 /Users/.../edinburgh-uni-learn-login/main.py
```

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

1. When running the executable you might get an `operation not found` error, this could mean that your file's
   been [quarantined](https://www.alansiu.net/2021/08/19/troubleshooting-zsh-operation-not-permitted/).

2. If your shell window stays open after the script's finished running, go to **Terminal** > **Preferences** > **
   Profiles** > **Shell** and change the default setting for when the shell exists from "don't close the window" to "
   close the window"
