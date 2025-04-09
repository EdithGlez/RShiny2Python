# PART 4 - Exercise 1 - Instructions

## Intro

You are building a simple To-Do tracker that allows you to create new tasks and
mark existing ones as completed. You are given an app that already takes care of
some server functionality (adding new tasks to an existing data frame)

## Tasks

- Add a data table output to the app, right above the `completed` button and
  show the current task list as a data frame
- When a row is selected and the `completed` button is clicked, that task should
  get the current time as a timestamp in the last column. Only one row can be
  selected at once
- When the button is clicked without a row being selected, nothing should happen

## Expected output

_The first two tasks have been marked as completed_

![screenshot](exercise1_screenshot.png)

## Shinylive Link

https://pieterjanvc.github.io/RShiny2Python/shinylive/?part4_ex1

## References

- [DataTable](https://shiny.posit.co/py/components/outputs/data-table/)
