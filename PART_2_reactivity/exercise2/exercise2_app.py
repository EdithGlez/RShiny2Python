# PART 2 - Exercise 2
# ///////////////////

import requests
import pandas as pd
from io import StringIO
from shiny import App, ui, render

# See README.md for instructions

# Get the data and process it
url = "https://data.opendatasoft.com/api/explore/v2.1/catalog/datasets/cats-in-movies@public/exports/csv"
resp = requests.get(url)
data = pd.read_csv(StringIO(resp.content.decode("UTF-8")), sep=";").sort_values(
    by=["title"]
)

# UI
app_ui = ui.page_fluid(
    ui.panel_title("Movies with cats"),
    ui.row(
        ui.column(
            4,
            ui.input_select("movie", "Movie", choices=data["title"].tolist()),
            ui.output_ui("img"),
        ),
        ui.column(
            8,
            ui.input_slider(
                "era",
                "Era",
                min=min(data["year"]),
                max=max(data["year"]),
                value=[min(data["year"]), max(data["year"])],
            ),
            ui.output_data_frame("tbl"),
        ),
    ),
)


# SERVER
def server(input, ouput, session):
    # Get the image URL from the data frame
    data[data["title"] == "Alien"]["url_poster"].values[0]

    # Filter the data frame by era (year range)
    data[(data["year"] >= 1950) & (data["year"] <= 1960)]

    # Select specific columns
    data[["year", "title", "produced_by", "directed_by"]]


app = App(app_ui, server)
