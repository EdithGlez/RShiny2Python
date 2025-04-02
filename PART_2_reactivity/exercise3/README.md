# PART 2 - Exercise 3 - Instructions

## Intro

```r
library(tidyverse)

data <- read_csv("PART_2_reactivity/exercise3/nutrients.csv") |> 
  filter(if_all(-Grams, function(x) {x != "t"})) |> 
  mutate(across(c(Calories:Carbs), function(x) as.numeric(str_remove_all(x, ",")))) |> 
  complete() |> select(-Measure)

nCals = 2100

data |> mutate(across(c(Grams:Carbs), function(x){
  x/Calories * nCals
}))

```

## Tasks

## Expected output


![screenshot](exercise3_screenshot.png)

## Shinylive Link
https://pieterjanvc.github.io/RShiny2Python/shinylive/?part2_ex3

## References

- [reactivity](https://shiny.posit.co/py/docs/reactive-foundations.html)
