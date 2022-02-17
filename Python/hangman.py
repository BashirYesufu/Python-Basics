#Step 1
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

display = []
word_length = len(chosen_word)
for letter in chosen_word:
  display += "_"
print(display)
  
guess = input("Guess a letter: ").lower()

for position in range(word_length):
  if chosen_word[position] == guess:
    display[position] = chosen_word[position]
print(display)
