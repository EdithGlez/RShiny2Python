# PART 1 - Exercise 1
# ////////////////////

from shiny import App, ui

app_ui = ui.page_fluid()


# You can ignore the sever function for this exercise
def server(input, output, session):
    pass


app = App(app_ui, server)
