#If the bill was ₦150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
bill = input("What was the total bill? ₦")
percent = input("What percentage tip would you like to give? 10, 12, 15? ")
people = input("How many people are going to split the bill? ")

total_bill_percent = (float(bill) * float(percent)) / 100
total_bill = float(bill) + total_bill_percent
pay_per_person = total_bill / float(people)

message = f"Each person should pay: ₦{round(pay_per_person, 2)}"
print(message)
