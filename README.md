# ChangeTerminalWorkingDirectory

> Terminal working directory changer for Windows, Linux and Mac.

## Table of Contents
* [General Info](#general-info)
* [Technologies](#technologies)
* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [Usage](#usage)
* [Description](#description)

## General Info
This project is a simple working directory changer CLI for Windows, Linux and Mac.

Every time I open a terminal, I have to change manually to the directory of the project I'm working on.
And it's a waste of time to do it manually every time. So I created this script to change the directory automatically.

## Technologies
* Python 3.x

## Prerequisites
* Python 3.x
* pip
* Git (optional)
* Terminal (cmd, bash, etc.)

## Setup
1. Clone the repository
```sh
git clone https://github.com/LimbersMay/changeTerminalDirectory.git
```

Rename the file **example.directories.json** to **directories.json** located in the folder **/config**.

### Linux and Mac
If you want to use the script without typing the full path, you have to add the script to the **PATH** variable 
and config an alias.

Usually the **PATH** variable is located in the file **.bashrc**, **.bash_profile** or **.zshrc**.

Now you can use the script in every directory by typing **changeTerminalDirectory** --option.

Example of how would look like the alias in the file **.bashrc**:
```sh
alias switchDir="python3 /path/to/changeTerminalDirectory/main.py"
```

### Usage

```sh
python main.py [-h] [-s ALIAS] [-a NAME] [-d ALIAS] [-l] [-r [PATH] [-g]
```

```sh
usage: change-dir [-h] [-s ALIAS] [-a NAME] [-d ALIAS] [-l] [-r [PATH] [-g]

options:
  -h, --help            show this help message and exit
  -s ALIAS, --switch ALIAS
                        Path to switch to.
  -a NAME, --alias NAME
                        Alias of the path to register.
  -d ALIAS, --delete ALIAS
                        Name of the path to delete.
  -l, --list            List all registered paths.
  -r [PATH], --register [PATH]
                        Register a path. If no path is given, the current path will be registered. If no alias is given, the alias will be last_path.
  -g, --goto-last       Move to the alias registered as last_path
```

### Description
* **-s** or **--switch** alias: Switch to the path registered with the given alias.
* **-r** or **--register** name with  **-a** or **--alias** name : Register the path given with the alias given.
* **-r** or **--register** with  **-a** or **--alias** name : Register the current path with the alias given.
* **-r** or **--register** : Register the current path with the alias **last_path**.
* **-d** or **--delete** alias : Delete the path registered with the given alias.
* **-l** or **--list** : List all registered alias with their path.
* **-g** or **--goto-last** : Switch to the path registered with the alias **last_path**.

### Examples
```sh
python main.py -r -a my_project
```

```sh
python main.py -r /path/to/my_project -a my_project
```
```
python main.py --register /path/to/my_project
```

```sh
python main.py --switch my_project
```
```sh
python main.py --delete my_project
```
```sh
python main.py --list
```
```sh
python main.py --goto-last
```
