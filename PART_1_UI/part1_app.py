# PART 1 - Live Demo
# //////////////////

from shiny import ui, render, App
from pathlib import Path

app_ui = ui.page_fluid(
    ui.layout_sidebar(
        ui.sidebar(ui.input_action_button("btn", "Click")),
        ui.input_text("txt", "Write some text"),
        ui.input_select("sel", "Choose:", choices=["Option 1", "Option 2"]),
        ui.output_text("outText"),
        ui.img(src = "image.jpg")
    )    
)

def server(input, output, session):
    pass

app = App(app_ui, server, static_assets=Path(__file__).parent / "exercise3" / "www")
