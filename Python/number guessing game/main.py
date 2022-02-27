#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from random import randint
from art import logo

print(logo)

# Compare the guess and answer for correctness
def check_answer(guess, answer):
  if guess > answer:
    print("Too high")
    return False
  elif guess < answer:
    print("Too low")
    return False
  else:
    print(f"You got it right. The answer is {answer}")
    return True

# Set the game's difficulty
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if level == "easy":
    return 10
  elif level == "hard":
    return 5

# Game logic
def game():
  print("Welcome to the guessing game")
  print("I am thinking of a number between 1 and 100")
  answer = randint(1, 100)
  
  turns = set_difficulty()
  print(f"You have {turns} attempts left to guess the number.")
  
  while turns > 0:
    guess = int (input("Make a guess: "))
    check_answer(guess, answer)
    if not check_answer(guess, answer):
      turns -= 1
    print(f"you have {turns} attempts left.")


game()
