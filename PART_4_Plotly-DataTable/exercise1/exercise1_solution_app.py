# PART 4 - Exercise 1 - Solution
# //////////////////////////////

from shiny import App, ui, reactive, render, req
import pandas as pd
from datetime import datetime

app_ui = ui.page_fluid(
    ui.card(
        ui.card_header("Create Task"),
        ui.input_text("task", "Description", width="auto"),
        ui.input_action_button("add", "Add task", width="150px"),
    ),
    ui.card(
        ui.card_header("ToDo list"),
        ui.output_data_frame("tbl"),
        ui.input_action_button(
            "completed", "Mark selected row as complete", width="300px"
        ),
    ),
)


def server(input, ouput, session):
    #  Start with empty data frame
    todos = reactive.value(pd.DataFrame())

    # Render the todos in the table
    @render.data_frame
    def tbl():
        return render.DataTable(todos(), selection_mode="row", width="100%")

    # Add a new todo
    @reactive.effect
    @reactive.event(input.add)
    def _():
        req(input.task().strip())
        newTask = pd.DataFrame(
            {
                "created": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
                "task": [input.task()],
                "completed": [None],
            }
        )
        todos.set(pd.concat([todos(), newTask], ignore_index=True))

    # Mark as completed based on selected row
    @reactive.effect
    @reactive.event(input.completed)
    def _():
        req(tbl.cell_selection()["rows"])
        updates = todos().copy()
        updates.at[tbl.cell_selection()["rows"][0], "completed"] = (
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        todos.set(updates)

app = App(app_ui, server)
