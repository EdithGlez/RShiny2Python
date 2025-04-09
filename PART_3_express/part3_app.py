# PART 3 - Live Demo
# //////////////////

from shiny.express import input, ui, render
from shiny import reactive

with ui.sidebar():
    ui.input_checkbox("chk", "Check")

    @render.text
    def out():
        if input.chk():
            return "Checked!"
        else:
            return "Not Checked"

ui.input_action_button("btn", "Click")

@reactive.effect
def _():
    print(input.btn())
