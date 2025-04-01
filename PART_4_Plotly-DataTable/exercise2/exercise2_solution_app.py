# PART 4 - Exercise 2 - Solution
# //////////////////////////////

from shiny import App, ui, reactive, render, req
import pandas as pd
from shiny import App, reactive, render, ui
from shinywidgets import output_widget, render_widget
import plotly.express as px
from pathlib import Path

# Edit data
file = "D:/Documents/LocalProjects/RShiny2Python/PART_4_Plotly-DataTable/exercise2/agenda.csv"
file = Path(__file__).parent / "agenda.csv"
df = pd.read_csv(file)
df['start'] = pd.to_datetime(df["start"], format="%Y-%m-%d %H:%M:%S")
df["track"] = df["start"].dt.day_name() + " - " + df["track"]   
df['end'] = pd.to_datetime(df["end"], format="%Y-%m-%d %H:%M:%S")
df['end'] = df['end'].apply(lambda x: x.replace(day=1))
df['start'] = df['start'].apply(lambda x: x.replace(day=1))

app_ui = ui.page_fluid(
    output_widget("plt")    
)

def server(input, output, session):
    
    @render_widget
    def plt():
        fig = px.timeline(df, x_start="start", x_end="end", y="track", hover_name = "title")
        fig.update_xaxes(tickformat="%H:%M", type = "date")       
        return fig

app = App(app_ui, server)
