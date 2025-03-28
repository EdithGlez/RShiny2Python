# PART 4 - Exercise 1
# ////////////////////

import pandas as pd
from shiny import App, ui, render, reactive

data = pd.DataFrame({
    "x": [1,2,3,4,5],
    "y": ["A", "B", "C", "D", "E"],
})

app_ui = ui.page_fluid(
  ui.output_data_frame("tbl")
)

def server(input, output, session):

    @render.data_frame
    def tbl():
        return render.DataTable(data, selection_mode = "row")

    @reactive.effect
    @reactive.event(tbl.cell_selection)
    def _():
        print(dir(tbl.cell_selection()))

app = App(app_ui, server)
