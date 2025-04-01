# PART 4 - Interactive Plots and Tables

## Intro

This workshop focuses on _Plotly_ for plots and _DataTables_ for tables, as both
are well integrated into the Shiny ecosystem and are available in both R and
Python. Shiny apps can monitor and capture clicks or other user events in these
interactive plots plots and tables, allowing additional server-side triggers.

_Note: This workshop does not focus on how to create plots or style tables, so
please refer to the respective libraries documentation for details_

## Interactive Data Tables

### Basic table

Data tables are part of the Shiny library in Python, so there is no need for any
additional installations

```python
app_ui = ui.page_fluid(
  ui.output_data_frame("tbl")
)

def server(input, output, session):

  @render.data_frame
  def tbl():
    return render.DataTable(df, selection_mode = "row")

```

_Note: code to generate `df` not shown_

- R uses `datatable` in function names (e.g. `datatableOutput()`) whereas Python
  mostly uses `data_frame`
- To set data table options, wrap the data frame in `render.DataTable`, similar
  to `datatable()` in R
- Set `selection_mode` to `none`, `row` or `rows` for row selection options

### Row selection event

With `selection_mode` set to 'row' or 'rows', you can observe the following:

```python
@reactive.effect
@reactive.event(tbl.cell_selection)
def _():
  print(tbl.cell_selection()["rows"])
```

- The returned **result is a tuple** of selected row indices
- Remember that **Python is 0-index based**, so the first row has index 0
- Note that in R, this process is different as the table is not accessible as an
  object and you use a modified input instead, e.g. `input$tbl_rows_selected`

## Interactive Plotly Plots

Unlike DataTables, Plotly is a separate library which has to be installed using
`pip install plotly`. Plotly comes with different APIs, with **Plotly Express**
being the most popular one. This is **not to be confused with Shiny Express** as
plotly express is used in both the Core and Express version of Shiny.

Plotly plots are widgets and Python Shiny comes with an additional library
called `shinywidgets` to interact with them.

_Note: This workshop is not focussing on creating Plotly plots, so all relevant 
code will be provided_

## Basic plotly plot

```python
import plotly.express as px
from shinywidgets import output_widget, render_widget

app_ui = ui.page_fluid(
  output_widget("plt")
)

def server(input, output, session):

    @render_widget
    def plt():
        return px.scatter(df, x = "age", y = "height")

```

_Note: code to generate `df` not shown_

- The generic `output_widget` is used as a UI placeholder for the plot, as this
  is not part of the standard UI library found in the `ui` object.
- Similarly, the decorator for the plot output is a custom `render_widget` one,
  though otherwise the function syntax is identical

### Data selection event

Observing specific events like clicking a point in a Plotly plot is currently
very different in Python Shiny than R and requires the use of another, lower
level plotly API called 'graph_objects'. Let's look at a full example below

```python
from shiny import App, reactive, render, ui
from shinywidgets import output_widget, render_widget
import plotly.express as px
import plotly.graph_objects as go

app_ui = ui.page_fluid(
    output_widget("plt"),
    ui.output_text("clicked")
)

def server(input, output, session):
    point_clicked = reactive.value([])

    def click_data(trace, points, selector):
        point_clicked.set(points.point_inds)

    @render_widget
    def plt():
        df = px.data.iris()
        fig = px.scatter(df, x="sepal_width", y="sepal_length")
        widget = go.FigureWidget(fig.data, fig.layout)
        widget.data[0].on_click(click_data)
        return widget

    @render.text
    def clicked():
        return f"Point Clicked: {point_clicked.get()}"


app = App(app_ui, server)

```

- Plotly plots are custom widgets that have a wrapper library shinywidgets
  making them useable in Shiny
- Use the custom output_widget in the UI and set the ID for your plotly plot. So
  don't use ui.output_plot in this case!
- Use the @render_widget decorator to create the reactive environment that
  creates the plot
- Create a normal plotly plot using the express syntax (e.g. px.scatter)
- Build the plotly widget by wrapping the plot into the FigureWidget function.
  Note that this function takes data and layout arguments, which you can get
  from the express plot
- To capture a trigger (e.g. click) add a custom function (e.g. click_data) to
  the widget using widget.data[0].on_click. This function contains info about
  the trace, points and selector. You can then update a reactive variable (e.g.
  point_clicked) using the info returned after a user click

## References

- [DataTable](https://shiny.posit.co/py/components/outputs/data-table/)
- [Plotly](https://shiny.posit.co/py/components/outputs/plot-plotly/)
