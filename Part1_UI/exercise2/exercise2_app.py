# PART 1 - Exercise 2 - Solution
# //////////////////////////////

# Create an app with two tabs (see exercise2_screenshot.png for expected layout)
# TAB 1:
#  - Sidebar layout with title: "Settings"
#  - In the side panel: Group of checkboxes called "Features" with options A, B, C
#  - In the main panel: Card with header "Info" and content paragraph "... some info ..."
# TAB 2:
#  - Table output (will be empty given no server yet)

from shiny import App, ui

app_ui = ui.page_fluid(
    
)

# Ignore for now
def server(input, ouput, session):
    pass


app = App(app_ui, server)
