# Student Marks and Grade Report

A small Python command-line exercise that collects a student's marks in Backend, Frontend, and Design, calculates the average, assigns a letter grade, and prints a report.

## Features

- Prompts for a student's name.
- Collects marks for three subjects: Backend, Frontend, and Design.
- Calculates the arithmetic average.
- Assigns a grade based on the average.
- Prints the student's marks, average, and grade.

## Grading scale

| Average | Grade |
| --- | --- |
| 80 and above | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| Below 50 | E |

## Requirements

- Python 3

No third-party packages are required.

## Run the program

From the repository root:

```bash
python report_generator.py
```

Follow the prompts and enter the student's name and three numeric marks.

## Current limitations

- The program does not currently validate that marks are within an expected range.
- It accepts numeric input only; non-numeric input will cause an error.
- The report is printed to the terminal and is not saved to a file.
- The script runs the report prompt when the file is executed.
