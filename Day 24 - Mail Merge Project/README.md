# Mail Merge Project

This project is part of my Python learning journey. It focuses on practicing core concepts like file I/O, directories, and path management.


## Overview

The program reads a list of names from a `.txt` file and merges each name into a generic letter template by replacing a placeholder. It then saves a personalized letter for each guest in the output folder.

## Features

- Reads names from a file
- Loads a template letter containing a placeholder (e.g., `[name]`)
- Replaces the placeholder with each actual name
- Outputs a new, personalized letter for each guest

## Technologies Used

- Python (basic file I/O, string manipulation, working with file paths)
- Standard libraries: `os`, `pathlib`

## Project Scenario

Suppose you're organizing an event and need to send out custom invitation letters. This script automates that by generating a personalized message for each person on your guest list.

## Example

Given:
- `Input/Names/invited_names.txt`
- `Input/Letters/starting_letter.txt`

The program will output:
- `Output/ReadyToSend/letter_for_John.txt`
- `Output/ReadyToSend/letter_for_Jane.txt`
- ...and so on.
