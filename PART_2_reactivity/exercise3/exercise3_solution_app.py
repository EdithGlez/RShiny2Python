# PART 2 - Exercise 3 - Solution
# //////////////////////////////

from shiny import App, ui, render, reactive
import seaborn as sns
import pandas as pd
from pathlib import Path

#data = pd.read_csv("PART_2_reactivity/exercise3/foods.csv")
data = pd.read_csv(Path(__file__).parent / "foods.csv")
data = data.sort_values("Food")

# UI
app_ui = ui.page_fluid(
    ui.panel_title("If I could only eat one thing ..."),
    ui.row(
        ui.column(
            4,
            ui.card(
                ui.card_header("Selection"),
                ui.input_select("food", "Pick a Food", choices=list(data["Food"])),
                ui.input_select(
                    "comp",
                    "Daily intake component to match",
                    choices=["Carbs", "Protein", "Fat", "Calories"],
                ),
            ),
        ),
        ui.column(
            8,
            ui.card(
                ui.card_header("Target Daily intake"),
                ui.row(
                    ui.column(
                        6,
                        ui.input_slider(
                            "Carbs", "Carbs (g)", min=10, max=500, value=250
                        ),
                        ui.input_slider(
                            "Protein", "Protein (g)", min=10, max=200, value=50
                        ),
                    ),
                    ui.column(
                        6,
                        ui.input_slider("Fat", "Fat (g)", min=10, max=200, value=60),
                        ui.input_slider(
                            "Calories", "kCals", min=1000, max=4000, value=2000
                        ),
                    ),
                ),
            ),
        ),
    ),
    ui.card(ui.card_header("Nutritional values"), ui.output_plot("plt")),
)


# SERVER
def server(input, output, session):

    @render.plot
    def plt():

        # Select food to focus e.g. Almonds
        food = data[data["Food"] == input.food()][
            ["Grams", "Calories", "Protein", "Fat", "Carbs"]
        ]
        # Get in long format
        food = pd.melt(food, var_name="name")
        # Adjust based on component to match and set daily target intake e.g. 250g of carbs
        food["value"] = (
            food["value"]
            / food.loc[food["name"] == input.comp(), "value"].values[0]
            * input[input.comp()]()
        )

        # Get the target daily intake values
        target = pd.DataFrame(
            {
                "name": ["Protein", "Fat", "Carbs"],
                "value": [input.Protein(), input.Fat(), input.Carbs()],
            }
        )
        # Create the bar plot showing consumed nutrients for chosen food
        plot = sns.barplot(
            x="name",
            y="value",
            data=food.iloc[2:5],
            color="#ff843d",
            label="Total Nutrients Consumed",
        )
        # Overlay barplot with target daily intake
        sns.barplot(
            x="name",
            y="value",
            data=target,
            color="gray",
            edgecolor="#007bc2",
            linewidth=2,
            facecolor="none",
            label="Recommended intake",
        )

        plot.set_ylabel("Grams")
        plot.set_xlabel("Nutrient")

        return plot


app = App(app_ui, server)
