# PART 4 - Interactive Plots and Tables

## Intro

One powerful feature of a Shiny app is the ability to capture clicks or other
user interaction in Plotly plots and Data Tables and react to them.

_Note: This workshop does not focus on how to create or style plots and tables,
so please refer to the respective libraries documentation for details_

## Interactive Data Tables

Data tables are part of the Shiny library in Python, so there is no need for any
additional installations

```python
app_ui = ui.page_fluid(
  ui.output_data_frame("tbl")
)

def server(input, output, session):

  @render.data_frame
  def tbl():
    render.DataTable(myDataFrame, selection_mode = "row")

```

- R uses `datatable` in function names (e.g. `datatableOutput()`) whereas Python
  mostly uses `data_frame`
- To set data table options, wrap the data frame in `render.DataTable`, similar
  to `datatable()` in R
- Set `selection_mode` to `none`, `row` or `rows` for row selection options

###

## References

- [Plotly](https://shiny.posit.co/py/components/outputs/plot-plotly/)
- [DataTable](https://shiny.posit.co/py/components/outputs/data-table/)
