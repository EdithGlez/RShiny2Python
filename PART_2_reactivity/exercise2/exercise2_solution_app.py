# PART 2 - Exercise 2 - Solution
# //////////////////////////////

import requests
import string
import random
from shiny import App, ui, render, reactive

# Get the data and process it
url = "https://raw.githubusercontent.com/david47k/top-english-wordlists/refs/heads/master/top_english_nouns_lower_10000.txt"
words = requests.get(url).text.splitlines()
words = [word for word in words if len(word) == 5]

# Select a random word every time the app reloads
word = random.choice(words)

# UI
app_ui = ui.page_fluid(
    ui.panel_title("Hangman"),
    ui.output_ui("progress"),
    ui.input_select("letter", "Pick a letter", choices=list(string.ascii_lowercase)),
    ui.input_action_button("guess", 'Guess'),
)


# SERVER
def server(input, ouput, session):

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
        
        #Update the guessed letters reactive
        guesses.set(x)
        
        return "".join([letter if letter in x else " - " for letter in list(word)])
    
    @render.ui
    def progress(): 
        out = f"<h1>{result()}</h1><h3>YOU WON!</h3>" if word == result() else \
            f"<h3>{result()}</h3>"
        return ui.HTML(out)


app = App(app_ui, server)
