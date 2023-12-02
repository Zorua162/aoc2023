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

### Day generation

Things that need updating in each template:

- Copy template folder
- Rename it to the current day name (for example dayx)
- Rename the solution file, so `dayx_solution.py` -> `day1_solution.py`
- Rename the test file, so `test_dayx.py` -> `test_day1.py`
- Update the import path in the test file
- Update the `current_day` variable in both files to be the name of the current folder

### Automation

These steps are automated by the script `generate_new_day.py`, which is run by giving
it the day number which is wished to be generated

## Pipelines

I'm planning to add a GitHub actions pipeline in the future, which will provide future
validation that my unit tests continue to work.

## Code standards

Pre-commit has been setup for this repo, which provides the standards that should be
followed. These standards are all automated, so as long as valid Python code is
submitted then commiting once with errors should automatically resolve themselves.

### Setup

To setup the pre-commits, first install pre-commit via the `dev-requirements.txt` file:
`python -m pip install -r requirements.txt`

Now setup the pre-commits in your local environment:
`pre-commit install`

Lastly, it is often useful to let pre-commit catch any files that it may have missed,
run: `pre-commit run --all`, then pre-commit will only run on changed files when they
are commited.

### Pre-commits used

- black: Automatically ensures that flake-8 is followed with a standardized style

- end of file fixer: Automatically ensures that every file has a new line at the end of
 it

- trailing whitespace: Remove whitespace
