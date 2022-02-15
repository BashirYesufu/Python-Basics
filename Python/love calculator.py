# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name = name1 + name2
lower_name_true = name.lower().count("t") + name.lower().count("r") + name.lower().count("u") + name.lower().count("e")
lower_name_love = name.lower().count("l") + name.lower().count("o") + name.lower().count("v") + name.lower().count("e")
love_score = int(str(lower_name_true) + str(lower_name_love))

if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and menthos")
elif love_score >= 40 or love_score <= 50:
  print(f"Your score is {love_score}, you are alright together")
else:
  print(f"Your score is {love_score}")


