# 🧑‍🏫 Vocabulary Teacher Project 🧑‍🏫

## Overview

The Vocabulary Teacher Project is designed to assist learners in expanding their vocabulary through targeted exercises and interactive learning tools. Central to this project is the `vocab_teacher.py` script, which plays a pivotal role in delivering personalized vocabulary instruction and assessments.

## Features

- **Interactive Learning Sessions**: Engages users with dynamic sessions where new words are introduced based on their learning progress, if you mark it as wrong it will appear again while words which you know won't appear again
- **Assessment and Feedback**: Keeps score many wrongs you get before you master all the words or a certain range of words.

## `vocab_teacher.py` Module

The `vocab_teacher.py` script functions as the core teaching assistant in this project. Here are its main responsibilities:

- **Word Selection**: Chooses words for sessions based on a predefined list or user performance. (excel format)
- **Session Management**: Set range of words you want to learn and reset the right/wrong counter.
- **User Interaction**: Use buttons or keybidings to have a smooth process of seeing definitions, examples and marking right and wrong.

## Setup

To set up the Vocabulary Teacher on your local machine, follow these steps:

1. Ensure that Python 3.x is installed.
2. Clone the repository or download the files directly.
3. Install the dependancies

## Other files:

`flashcard_gen.py` generates a pdf file that can be used to print flashcards by printing doublesided.

`populate_def.py` if you have a word list in excel with words, populates the definition column (does not work the best)
