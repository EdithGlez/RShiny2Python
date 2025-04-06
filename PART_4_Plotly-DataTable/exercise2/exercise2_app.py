# PART 4 - Exercise 2
# ///////////////////

from shiny import App, ui, reactive, render, req
from shiny import App, reactive, render, ui
from shinywidgets import output_widget, render_widget
import json
import pandas as pd
from pathlib import Path
import plotly.express as px
import plotly.graph_objects as go

# --- PROCESSING DATA

# Get the conference agenda
# file = "PART_4_Plotly-DataTable\\exercise2\\agenda.json"
file = Path(__file__).parent / "agenda.json"
with open(file, "r") as file:
    data = list(json.load(file).values())

# Function to convert JSON to text
def format_dict_with_bullets(d, indent=0):
    result = []
    for key, value in d.items():
        # Create an indent for nested dictionaries
        space = " " * indent
        if isinstance(value, dict):
            # If the value is a dictionary, call the function recursively
            result.append(f"{space}- {key}:")
            result.append(format_dict_with_bullets(value, indent + 4))
        else:
            # Otherwise, format the key-value pair as a bullet point
            result.append(f"{space}- {key}: {value}<br>")
    return "\n".join(result)

# Generate a data frame from the JSON file
df = pd.DataFrame(
    [
        {
            "track": item["track"],
            "start": item["start_time"],
            "end": item["end_time"],
            "title": item["title"],
            "color": item["colour"],
        }
        for item in data
    ]
)

# Create dates and tracks
df["start"] = pd.to_datetime(df["start"])
df["track"] = df["start"].dt.day_name() + " - " + df["track"]
df["end"] = pd.to_datetime(df["end"])
df["end"] = df["end"].apply(lambda x: x.replace(day=1))
df["start"] = df["start"].apply(lambda x: x.replace(day=1))
df["start"] = df["start"].dt.tz_localize("UTC").dt.tz_convert("US/Eastern")
df["end"] = df["end"].dt.tz_localize("UTC").dt.tz_convert("US/Eastern")

# --- APP

app_ui = ui.page_fluid(
    ui.panel_title("Shiny 2025 Conference Agenda"),
    output_widget("plt"), 
    ui.output_ui("details")
)

def server(input, output, session):

    # Code to generate a plotly timeline
    fig = px.timeline(
            df, x_start="start", x_end="end", y="track", hover_name="title"
        )
    # Format layout
    fig.update_xaxes(tickformat="%H:%M", type="date")
    fig.update_traces(marker=dict(color=df["color"]))
    fig.update_layout(plot_bgcolor="white", paper_bgcolor="white")

    # Code to generate the metadata as text (e.g. for first event)
    ui.h3(ui.HTML(format_dict_with_bullets(data[0])))

app = App(app_ui, server)
