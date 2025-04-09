# PART 1 - Exercise 3
# ///////////////////

from shiny import App, ui

#UI
app_ui = ui.page_fluid()

# Ignore for now
def server(input, output, session):
    pass


app = App(app_ui, server)
