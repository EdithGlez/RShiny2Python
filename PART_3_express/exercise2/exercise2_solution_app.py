# PART 3 - Exercise 2 - Solution
# //////////////////////////////
from pathlib import Path
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

# Dropdown for vehicle type
ui.input_select("vehicleType", "Vehicle Type", choices=vehicleTypes)

# Slider for minimum duration
ui.input_slider(
    "duration",
    "Minimum duration (min)",
    min=min(data["Duration"]),
    max=max(data["Duration"]),
    value=min(data["Duration"]),
)


# Slider update on vehicle type change
@reactive.effect
@reactive.event(input.vehicleType)
def _():
    df = data
    ui.update_slider(
        "duration",
        min=min(df["Duration"]),
        max=max(df["Duration"]),
        value=min(df["Duration"]),
    )


# Filtered table
@render.data_frame
def table():
    return data[
        (data["Duration"] >= input.duration())
        & data["Vehicle"].str.contains(str(input.vehicleType()))
    ]
