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
        ui.nav_panel("Tab 2", ui.output_table("tbl")),
    )
)


# Ignore for now
def server(input, ouput, session):
    pass


app = App(app_ui, server)
