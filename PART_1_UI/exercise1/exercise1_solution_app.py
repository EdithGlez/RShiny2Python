# PART 1 - Exercise 1 - Solution
# //////////////////////////////

from shiny import App, ui

app_ui = ui.page_fluid(
    ui.panel_title("Shiny Q&A"),
    ui.input_text("name", "Your Name"),
    ui.input_select(
        "category", "Category", choices=["General", "Development", "Deployment"]
    ),
    ui.input_text_area("question", "Question"),
    ui.input_action_button("send", "Send"),
)


# You can ignore the sever function for this exercise
def server(input, ouput, session):
    pass


app = App(app_ui, server)
