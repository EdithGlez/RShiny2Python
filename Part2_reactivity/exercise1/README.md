# PART 2 - Exercise 1 - Instructions

## Tasks

This app allows you to explore famous movies throughout cinematic history that
feature cats. The data is provided and UI has already been created. You will:

1. Populate the `img` output with an image HTML tag that contains the movie
   poster selected in the `movie` dropdown. The URL for each movie can be found
   in the `url_poster` column of the data frame (so no local images needed)

2. Render the data frame in the `tbl` output, ideally only showing the "year",
   "title", "produced_by", "directed_by" columns

3. Filter the data frame based on the year selection set by the `era` slider

## Expected output

![screenshot](exercise1_screenshot.png)

## Tips

### Convert a data frame column to a list

```python
df["name"].tolist()
```

### Filter a pandas data frame

```python
df[(df["a"] > 5) & (df["group"] == "test")]
```
- This example filters rows from a data frame based on two criteria
    - value a > 5 and the group name is "test"

## References

- [render outputs](https://shiny.posit.co/py/components/#outputs)
