# PART 1 - Exercise 2
# ///////////////////

from shiny import App, ui

app_ui = ui.page_fluid()


# Ignore for now
def server(input, ouput, session):
    pass


app = App(app_ui, server)
