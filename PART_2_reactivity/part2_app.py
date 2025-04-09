# PART 2 - Live Demo
# //////////////////

from shiny import App, reactive, render, ui

app_ui = ui.page_fluid(
    ui.input_numeric("num", "Number", 2),
    ui.input_action_button("btn", "Click"),
    ui.output_ui("out"), 
)

def server(input, output, session):
    
    @render.ui
    def out():
        return ui.HTML("The <b>square</b> of the number is: " + str(square()))
    
    @reactive.calc
    @reactive.event(input.btn)
    def square():
        return input.num() ** 2
    
    @reactive.effect
    @reactive.event(input.btn)
    def _():
        print(input.num())

app = App(app_ui, server)
