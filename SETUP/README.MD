# Setting up for the Workshop

As this workshop is about Shiny for Python, you need to have a python
environment set up so you can start creating your own apps.

- **Online with Shinylive**: This is recommended if you like to get stated
  quickly and do not have a local Python Shiny development environment setup
- **Local**: This setup is recommended if you have experience setting up new
  workspaces quicky and installing the various requirements, it will also
  provide the most comprehensive experience and you get to keep all of your work

## ONLINE USING SHINYLIVE

Shinylive allows you to build and run (simple) Shiny apps all from within the
browser without the need to install anything (e.g. no need to setup Python,
Shiny or even an IDE).

To learn more about the framework and its advantages and disadvantages, visit
the [shinylive documentation](https://shiny.posit.co/py/docs/shinylive.html)
website

### Access

You can access Shinylive for Python via https://shinylive.io/py/editor/

Note that for this workshop, **we will provide you with dedicated links for each
exercise** that already has start code and relevant files uploaded. These links
can be found in each exercise's README. You can at any point also copy-paste
code from this repo into the editor if needed or even upload files

### Uploading local data

NOTE: If you are using the dedicated links provided in each exercise's README in
this repository, you should not have to upload any data unless specifically
noted in the instructions.

- You can upload data from your computer into a shinylive app by clicking the
  add `+` icon next to the `app.py` file.
- To upload data to a subfolder, e.g. `www` add the relative path as part of the
  filename e.g. `www/image.png`
- Alternatively, you can upload the data elsewhere, make it publicly available
  and use links instead to read the data in dynamically. We will provide this
  option where needed

### Using external libraries

If your app requires additional libraries outside of the core python modules or
the shiny library, you can **add a `requirements.txt` file** (create from
scratch) and add the libraries there so they will be installed when you run the
app.

Note that not all Python libraries are available in Shinylive. For a full list
refer to the
[Pyodide website](https://pyodide.org/en/0.27.3/usage/packages-in-pyodide.html)

## LOCAL SETUP

### Step 1 - Clone this repository

- Git Clone: Navigate to the folder where you want to store this project and
  then run `git clone https://github.com/pieterjanvc/RShiny2Python.git`
- Manual Download:
  [Download](https://github.com/pieterjanvc/RShiny2Python/archive/refs/heads/main.zip)
  and Unzip the repo anywhere on your computer

### Step 2 - Make sure you have Python installed

To check your current, default Python version, run the following command on the
Terminal

```
python --version
```

_Python 3.13 was used whilst creating the exercises, but older versions should
work as well_

### Step 3 - Pick an IDE

It is highly recommended to choose an IDE that has extended Python support and
integrates well with Shiny. Below is a list of the IDE's in order of
recommendation.

#### Positron

Best if you code in both R and Python. This IDE is a fork of VS code, so if you
are familiar with the latter it will be very easy to adopt working in it.

1. Install [Positron](https://positron.posit.co/download.html)
2. Install the Shiny extension
   - Open the extension tab in Positron (ctrl/cmd + shift + x)
   - Search for `Posit.shiny` and install the extension
   - Reload if needed

#### Visual Studio (VS) Code

_Very similar to Positron, but recommended in case you use other programming
languages as well and prefer not to install another IDE_

1. Install [VS Code](https://code.visualstudio.com/)
2. Install the Shiny extension
   - Open the extension tab in Positron (ctrl/cmd + shift + x)
   - Search for `Posit.shiny` and install the extension
   - Reload if needed

#### R Studio Desktop

There is only limited support for using Python Shiny in RStudio, but if you
really prefer to work in it and don't want to use _shinylive_, you can make
this work. 

1. Open RStudio
2. Install the reticulate package `install.packages("reticulate")`
3. Set the Python interpreter: Tools --> Global Options --> Python

### Step 4 - Setup Environment and Install Packages

It is recommended to setup a virtual python environment to ensure you have all
the correct package versions, but this is optional.

- If you are using the built-in python environment manager use
  `requirements.txt` to install all dependencies
- If you are using [uv](https://docs.astral.sh/uv/), you can use the `uv.lock`
  file

Alternatively, install any required packages depending on the exercise you are
at using the basic pip command in the Terminal. For example:

```sh
pip install shiny
```

_This workshop has been tested with Shiny 1.3+. If you have an older version
already installed, add the `--upgrade` flag to this command to get the latest
version_

You can now try and run the [test_app.py](./test_app.py) file.

- If you are using **Positron or VS Code** can click the **Run button** located
  on the top-right of the file if you have the extension installed
- If you are using **RStudio** or would like to **Start the app from the
  Terminal** you run the following command

```sh
shiny run --reload --launch-browser test_app.py
```

_To stop the Shiny app, press ctrl/cmd + C in the terminal_
