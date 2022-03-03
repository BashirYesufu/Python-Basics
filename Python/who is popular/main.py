# import files
from random import randint
from art import logo, vs
from game_data import data
from replit import clear

# Track User score
score = 0
should_continue = True

# Generate random item from the game data
first = data[randint(0, len(data) - 1)]
second = data[randint(0, len(data) - 1)]

# Helper function to check correctness of user's answer
def check_popularity():
  if first['follower_count'] > second['follower_count']:
    return first['follower_count']
  elif first['follower_count'] < second['follower_count']:
    return second['follower_count']
  else:
    return first['follower_count']
  
# Method to check correctness
def compare_answer(input):
  highest_popularity = check_popularity()
  if input == 'a':
    if first['follower_count'] == highest_popularity:
      return True
    else:
      return False
  elif input == 'b':
    if second['follower_count'] == highest_popularity:
      return True
    else:
      return False
  else:
    print('You did not enter a valid option')
    return False

# Game logic
while should_continue:
  print(logo)
  print(f"Compare A: {first['name']}, a popular {first['description']} from {first['country']}")
  print(vs)
  print(f"Against B: {second['name']}, a popular {second['description']} from {second['country']}")
  
  # Collect User input
  user_answer = input(f"Who has more followers on instagram? Type 'A' for {first['name']} or 'B' for {second['name']}:\n").lower()

  # Clear screen in between rounds
  clear()
  print(logo)
  # Increment score
  if compare_answer(user_answer):
    score += 1
    if user_answer == 'a':
      print(f"You're right! {first['name']} has {first['follower_count']} million followers. Your score is {score}")
    else:
      print(f"You're right! {second['name']} has {second['follower_count']} million followers. Your score is {score}")
    first = second
    second = data[randint(0, len(data) - 1)]
  else:
    print(f"Sorry, that was wrong. Your final score is {score}. Game Over.")
    should_continue = False
  
  compare_answer(user_answer)
