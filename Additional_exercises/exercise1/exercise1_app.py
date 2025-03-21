# PART 1 - Exercise 1
# ///////////////////
import random

colours = ["red", "blue", "green", "yellow", "white", "black"]
guess = ["white", "red", "green", "blue"]
solution = random.choices(colours, k=4)


def check_guess(guess, solution):
    correctCol = 0
    colourAndPos = 0

    for g, s in zip(guess, solution):
        correctCol += 1 if g in solution and g != s else 0
        colourAndPos += 1 if g == s else 0

    won = True if colourAndPos == 4 else False

    feedback = (
        "Guess: " + "\t".join(guess) + "\t| " + "YOU WON!"
        if result["won"]
        else (
            str(result["correctCol"])
            + " correct colour; "
            + str(result["colourAndPos"])
            + " correct position"
        )
    )

    return {
        "won": won,
        "correctCol": correctCol,
        "colourAndPos": colourAndPos,
        "feedback": feedback,
    }


result = check_guess(guess, solution)

print(result["feedback"])
