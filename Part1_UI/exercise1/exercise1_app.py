# PART 1 - Exercise 1
# ////////////////////

# Recreate the layout as shown in the exercise1_screenshot.png
#  When you run the app, you should see a similar output (plot will be empty)

from shiny import App, ui

app_ui = ui.page_fluid()


# You can ignore the sever function for this exercise
def server(input, ouput, session):
    pass


app = App(app_ui, server)
