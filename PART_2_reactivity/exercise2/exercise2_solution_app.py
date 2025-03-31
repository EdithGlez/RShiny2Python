# PART 2 - Exercise 2 - Solution
# //////////////////////////////

import requests
import string
import random
from shiny import App, ui, render, reactive

# Get the data and process it
url = "https://raw.githubusercontent.com/pkLazer/password_rank/refs/heads/master/4000-most-common-english-words-csv.csv"
words = requests.get(url).text.splitlines()
words = [word for word in words if len(word) == 6]

# UI
app_ui = ui.page_fluid(
    ui.panel_title("Hangman"),
    ui.output_ui("progress"),
    ui.input_select("letter", "Pick a letter", choices=list(string.ascii_lowercase)),
    ui.input_action_button("guess", "Guess"),
)


# SERVER
def server(input, ouput, session):
    # Select a random word every time the app reloads
    word = random.choice(words)
    guesses = reactive.value([])

    @reactive.calc
    @reactive.event(input.guess)
    def result():
        # Add the new guess to the existing list
        x = guesses()
        x.append(input.letter())

        # Update the selection box
        remaining = [l for l in list(string.ascii_lowercase) if l not in x]
        ui.update_select("letter", choices=remaining)

        # Update the guessed letters reactive
        guesses.set(x)

        return " ".join([letter if letter in x else " - " for letter in list(word)])

    @render.ui
    def progress():
        return ui.h1(result(), style="font-family: monospace; color: #BF408B;")


app = App(app_ui, server)
