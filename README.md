# Toy Robot Simulator

REA Code Pairing exercise


## Prerequisites

Building/running requires a system with Python 3 installed and available on the
`PATH` as `python3`.

On some systems the command may be installed as `python` (for example, Windows),
so a substitution may be necessary.


### Setup a virtual environment (optional)

You can setup a virtual environment to install the dependencies, to avoid
installing conflicting packages into your global environment.

```sh
# create a venv
python3 -m venv venv
```

#### Activate the virtual environment

##### Mac OS X, Linux (bash-like shells)

```bash
source venv/bin/activate
```

##### Windows Command Prompt

```bat
.\venv\Scripts\activate
```

##### Windows PowerShell

```powershell
# it may be necessary to enable script execution for the session
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

.\venv\Scripts\Activate.ps1
```


### Install required dependencies

```sh
pip install -r requirements.txt
```


## Running tests

```sh
python3 -m pytest
```


## Running the application 

```sh
python3 main.py
```


## Using docker (optional)

If you don't have a Python 3 environment set up locally, you can use the below
command to start one. Note that docker requires the absolute path to mount, and
the way you get this may look different depending on your shell.

For example, for Windows Command Prompt, you can substitute `%cd%`, and for
Windows PowerShell, use `${PWD}`.

```sh
docker run --rm -it -v $(pwd):/home -w /home --entrypoint /bin/bash python:3
```
