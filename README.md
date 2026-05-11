# number-guessing-game

This is a simple, interactive command-line game built with Python. The program generates a random number between 1 and 10 and challenges the player to guess it, providing hints ("You guessed too high" or "Too low") until they find the correct answer.

## Features

- **Dynamic Feedback:** The program tells the player whether their guess is too high or too low.
- **Persistent Gameplay:** It uses a `while` loop to let the player keep guessing without restarting the script.
- **Input Validation:** It converts text input into integers for accurate mathematical comparison.

## How to Play

1. The game will prompt you to guess a number between 1 and 10.
2. Type your number and press `Enter`.
3. If you are incorrect, the game will print a hint and ask you to try again.
4. The game ends automatically when you guess the correct number.

## Code Overview

The project highlights core Python programming fundamentals:
- **Modules:** Importing and using the `random` module for generating targets.
- **Type Casting:** Converting string inputs from `input()` into integers using `int()`.
- **Control Flow:** Utilizing `while` loops for continuous execution and `if/else` conditional logic for hint systems.
