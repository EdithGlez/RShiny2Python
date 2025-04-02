# PART 3 - Exercise 2
# ///////////////////
import os
import pandas as pd
from datetime import datetime

from shiny import reactive
from shiny.express import input, render, ui, app_opts

data = pd.read_csv(
    "https://data.nasa.gov/api/views/9kcy-zwvn/rows.csv?accessType=DOWNLOAD"
)

# Data cleaning
data.columns = data.columns.str.replace(" ", "")
data["Date"] = pd.to_datetime(data["Date"])
data["Duration"] = pd.to_datetime(data["Duration"], format="%H:%M")
data["Duration"] = data["Duration"].dt.hour * 60 + data["Duration"].dt.minute
data = data.drop(["EVA#", "Country"], axis=1)
data = data.dropna()


# Get a simplified list of vehicle types
vehicleTypes = list(data["Vehicle"].str.extract(r"([^\s-]+)")[0].unique())
vehicleTypes.sort()

# Minimum duration in minutes
minDuration = 60

# Filter based on vehicleType and minimum duration
subset = data[
    (data["Duration"] >= minDuration) & data["Vehicle"].str.contains(vehicleTypes[0])
]

# Check the subset
subset
