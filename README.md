# Transferring your R Shiny skills to Python

_PJ Van Camp_

## Intro and Objectives

This repository contains materials used in the 'Transferring your R Shiny skills
to Python' workshop. The workshop aims to teach you how you can quickly start
building Shiny apps in Python if you already know R Shiny and have basic Python
coding skills.

This workshops has the following objectives:

- Describe the large conceptual overlap between R and Python Shiny
- Explain the differences between the Core and Express Python Shiny framework
- Demonstrate the power of Positron IDE for easily switching between R and
  Python Shiny
- Define decorators in Python and their use in the Shiny framework
- Convert core R Shiny functions (inputs, outputs, reactive environments) to
  Python syntax
- Build a few simple apps to showcase how easy the transition is
- Outline common R Shiny functionality that is not yet (fully) implemented in
  Python

## Setup

As this workshop is about Shiny Python, you need to make sure you have
everything set up to start creating your own apps.

### Step 1 - Make sure you have Python installed

Using the latest version is best, but try at least to have version 3.8+ To check
you Python version, run the following command on the Terminal

```
python --version
```

### Step 2 - Pick an IDE

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

#### Shinylive

In case of any issues in setting up a local IDE on your computer, shinylive can
be used where possible to complete exercises in the browser.

1. Open the Shinylive online editor (link below)
2. Copy any Shiny exercise code form this repo and paste it in the editor
3. Run the app tot test it
4. **Skip Step 3** below as this is only needed on local machines

_Note on working with local files in Shinylive_

- You can upload data from your computer into a shinylive app by clicking the
  add `+` icon next to the `app.py` file.
- To upload data to a subfolder, e.g. `www` add the relative path as part of the
  filename e.g. `www/image.png`
- Alternatively, you can upload the data elsewhere, make it publicly available
  and use links instead to read the data in dynamically. We will provide this
  option where needed

_Note that not all exercises might work given not all python packages / data are
available_

[Link to Shinylive for this workshop](https://shinylive.io/py/editor/#code=NobwRAdghgtgpmAXGKAHVA6VBPMAaMAYwHsIAXOcpMAYgAIBhACzkIGs7iBXMupssqgDOiAPSiA5gEsyTLgCMMJGKNRS4FAE4ArKBABuhUQCUAykykRsAJgAK2WaRpCLVgDZT9cADoR6dADNiTToYYLg6SyDOCD5iAHc6MmI6LiEIl0tsDy9A4KSWOnjgthdiVF8wAF88cGh4ak04AEcuKSb4ciEMMgAPMnwiUgoqZFQ9ABMoIV9UN2IyN2xKqoBdIA)

#### R Studio Desktop

There is only limited support for using Python in RStudio, but if you really
prefer to work in it, you can make this work. This option is only recommended if
you already have RStudio installed and do not want to install anything else.

1. Open RStudio
2. Install the reticulate package `install.packages("reticulate")`
3. Set the Python interpreter: Tools --> Global Options --> Python

### Step 3 - Install and Test Python Shiny

Run the following command in the terminal to install Shiny for Python

```sh
pip install shiny
```

_Note: If you are using RStudio, make sure to use the Terminal and not Console_

You can now try and run the [test_app.py](./test_app.py) file.

- If you are using **Positron or VS Code** can click the **Run button** located
  on the top-right of the file if you have the extension installed
- If you are using **RStudio** or would like to **Start the app from the
  Terminal** you run the following command

```sh
shiny run --reload --launch-browser test_app.py
```

_To stop the Shiny app, press ctrl/cmd + c in the terminal_
