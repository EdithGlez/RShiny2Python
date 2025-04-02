# PART 2 - Reactivity

The logic behind **reactivity in R Shiny is identical in Python**, so again
there are one-to-one translations between the various reactive components,
although there are **some differences in syntax** from time to time.

## Accessing inputs

- In R, inputs are accessed using `input$<inputId>` e.g. `input$btn`
- In Python, inputs are accessed using `input.<inputId>()` e.g. `input.btn()`

Note that **Python always uses parentheses `()` to access reactive objects**.
This is more consistent than in R.

## Intro to decorators

The major syntactic difference between R and Python Shiny is that **Python uses
decorators to turn ordinary functions into different reactive environments**,
whereas R Shiny has a dedicate function for each type fo reactive environment.

A decorator is a function annotation what will add additional functionality to
an existing function whenever it is evaluated. There is no need to know how
these decorators work, just how you assign them.

Decorators start with an `@` symbol followed by the decorator function name

```python
@customDecorator
def myFunction:
    return True
```

All Shiny decorators can be found in the `reactive` or `render` objects imported
via `from shiny import reactive, render`

## Assigning outputs

Every R Shiny render function has an equivalent decorator in Python. Different
from R is that there is no need to use the `output` object.

| Output | R render function | Python function decorator |
| ------ | ----------------- | ------------------------- |
| Text   | `renderText()`    | `@render.text`            |
| Table  | `renderTable()`   | `@render.table`           |
| Plot   | `renderPlot()`    | `@render.plot`            |
| UI     | `renderUI()`      | `@render.ui`              |
| ...    | ...               | ...                       |

```python
@render.text
def txt():
    return "Hello" + str(input.name())
```

- The **output function name** is the name of the **UI outputId**. In R shiny
  the example would have used `output$txt`
- The **decorator** defines what type of output is being created (see table)
- Similar to R, the value returned by the function must be compatible with the
  render type (e.g. in the example, this is text)
- Make sure to use the `return` keywords or the output won't be rendered

## Other Reactive Environments

Shiny has 4 main types of reactive environments that differ in how they react to
trigger and whether they return a reactive variable. In python, decorators are
again used to convert regular functions in different reactive environments. The
`reactive` object contains all relevant decorators.

| Environment behaviour              | R function        | Python decorators                      |
| ---------------------------------- | ----------------- | -------------------------------------- |
| Always trigger / Return nothing    | `observe()`       | `@reactive.effect`                     |
| Always trigger / Return variable   | `reactive()`      | `@reactive.calc`                       |
| Specific trigger / Return nothing  | `observeEvent()`  | `@reactive.effect` & `@reactive.event` |
| Specific trigger / Return variable | `eventReactive()` | `@reactive.calc` & `@reactive.event`   |

Examples

```python
@reactive.effect
def _():
    print(input.a() + input.b())
```

- This environment is identical to `observe()` in R
- Given this environment **does not return anything**, convention says to use
  the empty assignment operator `_` for the function name

```python
@reactive.calc
@reactive.event(input.a)
def sum():
   return input.a() + input.b()
```

- This environment is identical to `eventReactive()` in R
- This environment **returns a reactive variable** `sum()`
- The environment will **only trigger when input.a() changes**. Note that in the
  reactive.event decorator the parentheses after input.a are omitted (will cause
  error if used)

## Reactive variables

`reactive.value()` is the Python equivalent to `reactiveVal()` in R

- To **assign** a reactive variable use the
  `var = reactive.value(<initialValue>)` function.
- To **access** a reactive variable, use `var()` or `var.get()`
- To **update** a reactive varaible, use `var.set(<newValue>)`

_Note: there is no equivalent to R's `reactiveValues()`, as this can all be
achieved with the same `reactive.value()` function using a list or dictionary_

### Caution when updating reactive variables

Whenever you want to assign the content of a reactive variable to a local 
variable, you must copy it to avoid unexpected behaviour.

Example
```python
x = myval().copy()
_ = x.pop()
myval.set(x)
```
