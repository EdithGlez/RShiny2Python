# Dummy Shiny App to test installation
from shiny import ui, App

app_ui = ui.page_fluid(ui.h1("Python Shiny is working!"))


def server(Inputs, Outputs, Session):
    pass


app = App(app_ui, server)
