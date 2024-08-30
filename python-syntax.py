"""
Question 1. Showcase Your Dance Moves!
Python Indentation Practice with if Statements

Task 1: Code Correction Below is a piece of Python code with incorrect indentation. Your task is to correct it."""
# weather = "sunny"

# if weather == "sunny":
# print("Wear sunglasses!")
# else:
# print("Take an umbrella!")


weather = "sunny"
if weather == "sunny":
    print("Wear sunglasses!")
else:
    print("Take an umbrella!")

"""
Task 2: Your Mood Today Ask the user how they feel today. If they say "happy", print "That's great to hear!", and if they say "sad", print "I hope your day gets better!". 
"""

user_input = input("How are you feeling today? (happy/sad) ")
if user_input == "happy":
    print("That's great to hear!")
elif user_input == "sad":
    print("I hope your day gets better!")
else:
    print("Should we try again?")


"""
Question 2. Python Naming Convention Practice
Task 1:Code Correction
"""

# Pi_value = 3.14
# userAge = 25
# user_location = "New York"
# MAXLIMIT = 1000

PI = 3.14
user_age = 25
user_location = "New York"
MAX_LIMIT = 1000

"""
Question 3. Arithmetic Operations in Daily Life

Task 1: Grocery Store Math Calculate the total cost of three items you'd commonly find in a grocery store, given their individual prices. For example, what would be the cost of bread, peanut butter, and jelly be? Prices don't need to be realistic!
"""

bread_price = 2.50
peanut_butter_price = 3.00
jelly_price = 1.50

total_cost = bread_price + peanut_butter_price + jelly_price
print(f"The total cost of bread, peanut butter, and jelly is ${total_cost:.2f}.")

"""
Task 2: Bank Interest 
If you have a savings account with a particular initial amount and a fixed yearly interest rate, calculate the total amount in your account after a year. So if you had $10,000 at a 7% interest write code that would tell us the amount at the end of the year. For the example the expected outcome would be $10,700.
"""

initial_amount = 10000
interest_rate = 0.07

total_amount = initial_amount + (initial_amount * interest_rate)
print(f"After a year, your account will have ${total_amount:.2f} ")