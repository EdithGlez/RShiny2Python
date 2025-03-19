# PART 1 - Exercise 1 - Solution
# //////////////////////////////
import random
from shiny import App, ui, reactive, render

colours = ["red", "blue", "green", "yellow", "white", "black"]

def check_guess(guess, solution):
        correctCol = 0
        colourAndPos = 0

        for g, s in zip(guess, solution):
            # correctCol FIX THIS - Incorrect logic
            correctCol += 1 if g in solution and g != s else 0
            colourAndPos += 1 if g == s else 0

        won = True if colourAndPos == 4 else False

        feedback = (
            "Guess: " + "\t".join(guess) + "\t| " + ("YOU WON!"
            if won
            else (
                str(correctCol)
                + " correct colour; "
                + str(colourAndPos)
                + " correct position"
            ))
        )

        return {
            "won": won,
            "correctCol": correctCol,
            "colourAndPos": colourAndPos,
            "feedback": feedback,
        }

app_ui = ui.page_fixed(
    ui.output_text_verbatim("progress"),
    ui.hr(),
    ui.row(
        ui.column(3, ui.input_select("a", None, choices=colours)),
        ui.column(3, ui.input_select("b", None, choices=colours)),
        ui.column(3, ui.input_select("c", None, choices=colours)),
        ui.column(3, ui.input_select("d", None, choices=colours)),
    ),
   
    ui.input_action_button("guess", "Guess")
    
)

def server(input, ouput, session):

    solution = random.choices(colours, k=4)
    log = reactive.value("--- Welcome to the Mastermind Game! ---")

    guess = ["white", "red", "green", "blue"]

    @reactive.effect
    @reactive.event(input.guess)
    def _():
        guess = [input.a(),input.b(),input.c(),input.d()]
        result = check_guess(guess, solution)
        log.set(log() + "\n" + result["feedback"])
    
    @render.text
    def progress():
        return log()

    

    result = check_guess(guess, solution)

    print(result["feedback"])

app = App(app_ui, server)

