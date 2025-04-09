# PART 1 - Exercise 3 - Solution
# //////////////////////////////

from shiny import App, ui
from pathlib import Path

#UI
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
        ui.nav_panel("Tab 2", ui.img(src="image.jpg")),
    )
)


# Ignore for now
def server(input, output, session):
    pass


app = App(app_ui, server, static_assets=Path(__file__).parent / "www")
