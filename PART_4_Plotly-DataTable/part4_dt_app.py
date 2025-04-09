
# PART 4 - Live Demo - Data Table
# ///////////////////////////////

from shiny import App, reactive, render, req, ui
import pandas as pd

info = pd.DataFrame({"x": [1,2,3], "y": ["A", "B", "C"]})

app_ui = ui.page_fluid(
    ui.output_data_frame("tbl"),
    ui.output_text("out"),
)


def server(input, output, session):
    @render.data_frame
    def tbl():
        return render.DataTable(info, selection_mode="row")

    @render.text
    def out():
        req(tbl.cell_selection()["rows"])        
        return info.iloc[tbl.cell_selection()["rows"][0]]["y"]

app = App(app_ui, server)
