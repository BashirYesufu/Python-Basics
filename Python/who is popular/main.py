# import files
from random import randint
from art import logo, vs
from game_data import data

# Generate random item from the game data
first = data[randint(0, len(data) - 1)]
second = data[randint(0, len(data) - 1)]

# Game logic
print(logo)
print(first)
print(second)
print(len(data))
print(vs)
