# PART 3 - Exercise 2 - Solution
# //////////////////////////////
import os
from shiny.express import input, render, ui, app_opts

# Set the www folder for static assets
app_opts(static_assets=os.path.join(os.path.dirname(__file__), "www"))


with ui.navset_card_tab(id="tab"):  
    # Tab 1
    with ui.nav_panel("YOUNG"):
        with ui.layout_columns(col_widths = [3, 9]):
            with ui.card():
                ui.img(src="young.png")
            with ui.card():
                ui.p("How it all began ...")
    # Tab 2
    with ui.nav_panel("ADULT"):
        with ui.layout_columns(col_widths = [3, 9]):
            with ui.card():
                ui.img(src="adult.png")
            with ui.card():
                ui.p(" ... what I aspired to ...")
    # Tab 3
    with ui.nav_panel("OLD"):       
        with ui.layout_columns(col_widths = [3, 9]):
            with ui.card():
                ui.img(src="old.png")
            with ui.card():
                ui.p("... what I have become")
