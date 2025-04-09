
# PART 4 - Live Demo - Plotly
# ///////////////////////////

from shiny import App, reactive, render, req, ui
from shinywidgets import output_widget, render_widget
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

app_ui = ui.page_fluid(    
    output_widget('plotly'),
	ui.output_text("out"),
)

info = pd.DataFrame({"x": [1,2,3], "y": ["A", "B", "C"]})

def server(input, output, session):

    bar = reactive.value()

    @render.text
    def out():
        return "You clicked bar " + str(bar() + 1)
	
    def plotly_click(trace, points, selector):
        bar.set(points.point_inds[0])

    @render_widget
    def plotly():
        x = px.bar(info, x = "x", y = "y")
        plt = go.FigureWidget(x.data, x.layout)
        plt.data[0].on_click(plotly_click)
        return plt   

app = App(app_ui, server)
