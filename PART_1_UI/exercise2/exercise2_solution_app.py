# PART 1 - Exercise 2 - Solution
# //////////////////////////////

from shiny import App, ui
import os

app_ui = ui.page_fluid(
    ui.navset_tab(
        ui.nav_panel(
            "Tab 1",
            ui.layout_sidebar(
                ui.sidebar(
                    ui.input_checkbox_group("cbx", "Features", choices=["A", "B", "C"]),
                    title="Settings",
                ),
                ui.card(ui.card_header("Info"), ui.p("... some info ...")),
            ),
        ),
        ui.nav_panel("Tab 2", ui.img(src="image.png")),
    )
)


# Ignore for now
def server(input, ouput, session):
    pass


app = App(app_ui, server, static_assets=os.path.join(os.path.dirname(__file__), "www"))
