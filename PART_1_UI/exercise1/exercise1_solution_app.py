# PART 1 - Exercise 1 - Solution
# //////////////////////////////

# Recreate the layout as shown in the exercise1_screenshot.png
#  When you run the app, you should see a similar output (plot will be empty)

from shiny import App, ui

app_ui = ui.page_fluid(
    ui.h1("Python Shiny Survey"),
    ui.row(
        ui.column(
            5,
            ui.input_slider(
                "exp",
                "Experience from 0 (none) to 5 (expert)",
                min=0,
                max=5,
                value=2,
            ),
            ui.input_select(
                "usage",
                "I write Python Shiny apps ...",
                choices=["Daily", "Weekly", "Monthly", "Yearly"],
            ),
            ui.hr(),
            ui.input_checkbox("preference", "I prefer Python Shiny over R Shiny"),
            ui.input_text_area("learn", "What would you like to learn more about?"),
        ),
        ui.column(7, ui.output_plot("plt")),
    ),
    ui.input_action_button("submit", "Submit"),
)


# You can ignore the sever function for this exercise
def server(input, ouput, session):
    pass


app = App(app_ui, server)
