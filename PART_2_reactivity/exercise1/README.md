# PART 2 - Exercise 1 - Instructions

## Intro

This app allows you to explore famous movies throughout cinematic history that
feature cats. The data is provided and UI has already been created. You should
be able to complete this exercise by just using render functions.

## Tasks

1. Populate the `img` output with an image HTML tag that contains the movie
   poster selected in the `movie` dropdown. The URL for each movie can be found
   in the `url_poster` column of the data frame (so no local images needed)

2. Render the data frame in the `tbl` output, only showing the "year", "title",
   "produced_by", "directed_by" columns

3. Filter the data frame based on the year selection set by the `era` slider

_Some example python code has been provided demonstrating how to manipulate
pandas data frames for this app as this is not the focus of this workshop_

## Expected output

![screenshot](exercise1_screenshot.png)

## Shinylive Link
https://pieterjanvc.github.io/RShiny2Python/shinylive/?part2_ex1

## References

- [render outputs](https://shiny.posit.co/py/components/#outputs)
