# PART 4 - Exercise 2
# ///////////////////

from shiny import App, ui, reactive, render, req
import pandas as pd
from shiny import App, reactive, render, ui
from shinywidgets import output_widget, render_widget
import plotly.express as px
import plotly.graph_objects as go

app_ui = ui.page_fluid(
    
)


def server(input, output, session):
    pass

app = App(app_ui, server)
