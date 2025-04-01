# PART 4 - Exercise 2 - Solution
# //////////////////////////////

from shiny import App, ui, reactive, render, req
import pandas as pd
from shiny import App, reactive, render, ui
from shinywidgets import output_widget, render_widget
import plotly.express as px
import plotly.graph_objects as go
import json
from pathlib import Path

# --- PROCESSING DATA
def format_dict_with_bullets(d, indent=0):
    result = []
    for key, value in d.items():
        # Create an indent for nested dictionaries
        space = " " * indent
        if isinstance(value, dict):
            # If the value is a dictionary, call the function recursively
            result.append(f"{space}- {key}:")
            result.append(format_dict_with_bullets(value, indent + 4))
        else:
            # Otherwise, format the key-value pair as a bullet point
            result.append(f"{space}- {key}: {value}<br>")
    return "\n".join(result)

file = "PART_4_Plotly-DataTable\\exercise2\\agenda.json"
file = Path(__file__).parent / "agenda.json"

with open(file, 'r') as file:
    data = list(json.load(file).values())

df = pd.DataFrame([{
    'track': item['track'],
    'start': item['start_time'],
    'end': item['end_time'],
    'title': item['title']
} for item in data])

df['start'] = pd.to_datetime(df["start"])
df["track"] = df["start"].dt.day_name() + " - " + df["track"]   
df['end'] = pd.to_datetime(df["end"])
df['end'] = df['end'].apply(lambda x: x.replace(day=1))
df['start'] = df['start'].apply(lambda x: x.replace(day=1))
df['start'] = df['start'].dt.tz_localize('UTC').dt.tz_convert('US/Eastern')
df['end'] = df['end'].dt.tz_localize('UTC').dt.tz_convert('US/Eastern')

# --- APP

app_ui = ui.page_fluid(
    output_widget("plt"),
    ui.output_ui("details")  
)

def server(input, output, session):
    point_clicked = reactive.value()

    def click_data(trace, points, selector):
        print(points.point_inds[0])
        point_clicked.set(points.point_inds[0])
    
    @render_widget
    def plt():
        fig = px.timeline(df, x_start="start", x_end="end", y="track", hover_name = "title")
        fig.update_xaxes(tickformat="%H:%M", type = "date")       
        widget = go.FigureWidget(fig.data, fig.layout)
        widget.data[0].on_click(click_data)
        return widget
    
    @render.ui
    def details():
        req(point_clicked() >= 0)
        return ui.h3(ui.HTML(format_dict_with_bullets(data[point_clicked()])))

app = App(app_ui, server)
