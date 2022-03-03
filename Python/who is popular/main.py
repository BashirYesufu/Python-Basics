# import files
from random import randint
from art import logo, vs
from game_data import data

# Generate random item from the game data
first = data[randint(0, len(data) - 1)]
second = data[randint(0, len(data) - 1)]

# Game logic
print(logo)
print(f"Compare A: {first['name']}, a popular {first['description']} from {first['country']}")
print(vs)
print(f"Against B: {second['name']}, a popular {second['description']} from {second['country']}")

print(first)


print(second)

user_answer = input(f"Who has more followers on instagram? Type 'A' for {first['name']} or 'B' for {second['name']}:\n").lower()

def check_popularity():
  if first['follower_count'] > second['follower_count']:
    return first['follower_count']
  elif first['follower_count'] < second['follower_count']:
    return second['follower_count']
  else:
    return first['follower_count']

def compare_answer(input):
  highest_popularity = check_popularity()
  if input == 'a':
    if first['follower_count'] == highest_popularity:
      print('Got it')
    else:
      print('Did not get it for a')
  elif input == 'b':
    if second['follower_count'] == highest_popularity:
      print('Got it')
    else:
      print('Did not get it from b')
  else:
    print('You did not enter a valid option')

compare_answer(user_answer)
