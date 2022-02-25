############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
import random
from replit import clear

# Add to the computer or user cards
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

# Sum up the cards and return the value
def calculate_score(card):
  if sum(card) == 21 and len(card) == 2:
    return 0
  if 11 in card and sum(card) > 21:
    card.remove(11)
    card.append(1)
  return sum(card)

# Check cards
def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, Opponent has a blackjack! 😱"
  elif user_score == 0:
    return "Win with a blackjack! 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😀"
  else:
    return "You lost 😤"
    
def play_game():
  user_cards = []
  computer_cards = []
  game_over = False
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"  Your cards: {user_cards}, current score: {user_score}")
    print(f"  Computer's first card: {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
      if user_should_deal == 'y':
        user_cards.append(deal_card())
  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(f"  Your final hand: {user_cards}, final_score: {user_score}")
  print(f"  Computer's final hand: {computer_cards}, final_score: {computer_score}")
  print(compare(user_score, computer_score))


while input("Do you want to play a new game? Type 'y' or 'n': ").lower() == "y":
  clear()
  play_game()
