# Zorua162's Advent of code 2023

## Plan

Get as far in AOC 2023 as I can, using methods I've learned throughout the year, like
unit testing, as I go.

## Template

```bash
template/
├── data.txt
├── dayx_solution.py
├── part1_example_data.txt
├── part2_example_data.txt
└── test_dayx.py
```

I've written myself a template, which I'm hoping to copy paste each day, to save the
time that it takes me to write the boiler plate of my solutions so that I can get
straight to solving the problem, these will likely evolve over time to make them easier
to use, so each day might not use exactly the same one.

Things that need updating in each template:

- Copy template folder
- Rename it to the current day name (for example dayx)
- Rename the solution file, so `dayx_solution.py` -> `day1_solution.py`
- Rename the test file, so `test_dayx.py` -> `test_day1.py`
- Update the import path in the test file
- Update the `current_day` variable in both files to be the name of the current folder
