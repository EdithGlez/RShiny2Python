

import requests
import pandas as pd
from io import StringIO
from shiny import App, ui, reactive, render

resp = requests.get("https://data.opendatasoft.com/api/explore/v2.1/catalog/datasets/cats-in-movies@public/exports/csv")
data = pd.read_csv(StringIO(resp.content.decode("UTF-8")), sep = ";")

app_ui = ui.page_fluid(
    ui.panel_title("Movies with cats"),
    ui.input_select("movie", "Movie", choices=data["title"]),
    ui.output_ui("img")
)

def server(input, ouput, session):

    @render.ui
    def img():
        return ui.img(src = data.iloc[int(input.movie())]["url_poster"])

app = App(app_ui, server)
