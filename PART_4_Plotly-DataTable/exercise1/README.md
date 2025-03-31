# PART 3 - Exercise 1 - Instructions

## Intro

You are creating a simple biography website template people can use to highlight
specific events in their lifetime that have shaped them.

## Tasks

### PART 1 - Simple express layout

Use Shiny express to create this site with 2 tabs (navset_card_tab)

- Each tab represents a stage in the life of the person
- Each tab has two columns
  - (width 3) A card with an image of the person
  - (width 9) A card with a paragraph of text
- The images are located in the `www` folder and some text has been provided.
  (_scroll down to see what to do if you are using shinylive_)

### PART 2 - Generating express UI with a function

- Create a function that will generate the repeating tab layout and has the
  following arguments:
  - tab: The name of the tab
  - image: Link to the image being displayed
  - text: paragraph of text
- Add a 3rd tab using the function
- Replace the first 2 tabs using the function as well to avoid repetition

_Tip: You will need the `@expressify` decorator to make your function work_

## Expected output

_Note that the 3rd tab should only be there for PART 2_

![screenshot](exercise1_screenshot.png)

## References

- [layouts](https://shiny.posit.co/py/layouts/)
- [expressify](https://shiny.posit.co/py/api/express/express.expressify.html)

#### _if you are using Shinylive_

You cant access images from your local machine in Shinylive, so use the
following URLs instead:

- Young: https://pieterjanvc.github.io/RShiny2Python/assets/young.jpg
- Adult: https://pieterjanvc.github.io/RShiny2Python/assets/adult.jpg
- Old: https://pieterjanvc.github.io/RShiny2Python/assets/old.jpg
