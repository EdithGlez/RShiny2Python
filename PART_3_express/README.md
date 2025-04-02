# PART 3 - Shiny Express

## Intro

Unlike in R, Shiny for Python has two implementations of the framework

- Core: Most stable version with all features and structured implementation
- Express: Quick to write, flexible with less boiler plate code

So far **you have been using the Core framework**, and this is what the majority
of this workshop outside of this module focusses on.

- Use Express syntax for quick prototyping or simple apps
- Choose the core framework for larger, more complex apps
- Express syntax does not have all features, like complex layout, modules,
  dynamic UI etc (see references for details)

## Express Syntax differences with Core

### Setup

Unlike in Core, Shiny Express does not have a dedicated organisation of UI and
server in separate functions, but rather makes use of decorators and context
managers. This means that regular Python code and Shiny specific syntax can be
mixed allowing a more fluid organisation of your code.

Note that you **import objects from `shiny.express` instead of `shiny`**

```python
from shiny.express import input, render, ui, app_opts
```

- There is no need to use the `App` function at the end of the page as you would
  with the Core framework
- If you want to set app options like static assets, you can use `app_opts`

```python
app_opts(static_assets=os.path.dirname(__file__), "myFolder"))
```
### Layout + inputs

Given there is **no dedicated UI** function. Layout is organised using **context
managers** using the `with` statement.

```python
with ui.sidebar():
    ui.input_slider("slider", "Pick a value", 0, 5, 0)
```

_This generates a sidebar layout with an input slider in it_

If you now want to add something to the "main" panel, just put it outside of the
context manager

```python
with ui.sidebar():
    ui.input_slider("slider", "Pick a value", 0, 5, 0)

ui.input_select("sel", "Choose", choices = ["A", "B", "C"])
```

- The slider will be in the side bar
- The select input will be in the main panel
- You can nest context managers to create more elaborate layouts

### Outputs

As again there is no dedicated server function, but any function can be made
reactive using the appropriate decorators.

- There are no dedicated UI placeholders for outputs. This means that functions
  that return an output (e.g. table, plot) it will insert it wherever it's been
  declared.
- Outputs can be declared inside of a context manager and will then appear in
  that part of the UI

```python
with ui.sidebar():
    ui.input_slider("slider", "Pick a value", 0, 5, 0)

    @render.text
    def sliderInfo():
        return f"You chose: {input.slider()}"

@render.ui
def picture():
    return ui.img(src = f"https://picsum.photos/id/{input.slider() + 10}/200/300",
                      height = "300px", width = "200px")

```

- The text output from `sliderInfo` will appear inside the sidebar underneath
  the slider itself
- The `picture` output will appear in the main panel

### Other reactive functions

Functions decorated with `@reactive.effect`, `@reactive.calc` and
`@reactive.event` can be placed anywhere in the script. In case they produce an
output, this can again be used in any other reactive environment (i.e. decorated
function)

Note: all code defined outside of a reactive function will only be run once at
startup. Given there is no server, all code will be run every time a new
instance starts.

## References

- [Core vs Express](https://shiny.posit.co/py/docs/express-vs-core.html)
- [Layouts](https://shiny.posit.co/py/layouts/)
- [Express full documentation](https://shiny.posit.co/py/api/express/)
