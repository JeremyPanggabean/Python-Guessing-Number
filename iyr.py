# 2D
fruits =     ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats =      ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

# print(groceries[2])
# print(groceries[2][2])
# for collection in groceries:
#     for food in collection:
#         print(food, end=" ")
#     print()
# for food in groceries:
#     for item in food:
#         print(item, end=", ")
#     print()

# num_pad = ((1, 2, 3),
#            (4, 5, 6),
#            (7, 8, 9),
#            ("*", 0, "#"))
#
# for row in num_pad:
#     for num in row:
#         print(num, end=" ")
#     print()

# Python quiz game
# questions = ("How many elements are in the periodic table?: ",
#              "Which animal lays the largest eggs?: ",
#              "What is the most abundant gas in Earth's atmosphere?: ",
#              "How many bones are in the human body?: ",
#              "Which planet in the solar system is the hottest?: ")
#
# options = (("A. 116", "B. 117", "C. 118", "D. 119"),
#            ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
#            ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
#            ("A. 206", "B. 207", "C. 208", "D. 209"),
#            ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))
#
# answers = ("C", "D", "A", "A", "B")
# guesses = []
# score = 0
# question_num = 0
#
# for question in questions:
#     print("-----------------")
#     print(question)
#     for option in options[question_num]:
#         print(option)
#     guess = input("Enter (A, B, C, D): ").upper()
#     guesses.append(guess)
#     if guess == answers[question_num]:
#         score += 1
#         print("CORRECT!")
#     else:
#         print("INCORRECT!")
#         print(f"{answers[question_num]} is the correct answer")
#     question_num += 1
#
#
# print("-----------------------")
# print("         RESULTS       ")
# print("-----------------------")
#
# print("answers: ", end="")
# for answer in answers:
#     print(answer, end=" ")
# print()
#
# print("guesses: ", end="")
# for guess in guesses:
#     print(guess, end=" ")
# print()
#
# score = int(score / len(questions) * 100)
# print(f"Your score is: {score}%")

# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}
# print(help(capitals))
# print(capitals.get(""))
# if capitals.get("India"):
#     print("That capital exist")
# else:
#     print("That capital doesn't exist")

# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "NY"})
# capitals.pop("USA")
# capitals.popitem()
# capitals.clear()
# print(capitals.keys())
# keys = capitals.keys()
# print(capitals.values())
# print(keys)
# for key in capitals.keys():
#     print(key, end=", ")
# print()
# for i in capitals.values():
#     print(i, end=" ")
# keys = list(capitals.values())
# i = 0
# while i < len(keys):
#     print(keys[i], end=" ")
#     i += 1

# items = capitals.items()
# print(items)

# for key, value in capitals.items():
#     print(f"{key}: {value}")

# Concession stand program

# # dictionary {key: value}
# menu = {"pizza": 3.00,
#         "nachos": 4.50,
#         "popcorn": 6.00,
#         "fries": 2.50,
#         "chips": 1.00,
#         "pretzel": 3.50,
#         "soda": 3.00,
#         "lemonade": 4.25}
#
# cart = []
# total = 0
#
# print("---------MENU---------")
# for key, value in menu.items():
#     print(f"{key:10}: ${value:2f}")
# print("-----------------------")
#
# while True:
#     food = input("Select an item (q to quit): ").lower()
#     if food.lower() == "q":
#         print("Thankyou")
#         break
#     elif menu.get(food) is not None:
#         cart.append(food)
#
# print("-------------YOUR ORDER------------------")
# for food in cart:
#     total += menu.get(food)
#     print(food, end=" ")
#
# print()
# print(f"Total is: ${total:.2f}")

import random
# print(help(random))

# low = 1
# high = 10
# options = ("rock", "paper", "scissors")
# cards = ["2", "3", "5", "8", "Q", "U", "I", "O"]
#
# # number = random.randint(low, high)
# # number = random.random()
# # option = random.choice(options)
# random.shuffle(cards)
#
# print(cards)

# import random
#
# lowest_num = 1
# highest_num = 100
# answer = random.randint(lowest_num, highest_num)
# guesses = 0
# is_running = True
#
# print("---------------Python Number Guessing Game---------------")
# print(f"Select a number between {lowest_num} and {highest_num}")
#
# while is_running:
#     guess = input("Enter your guess: ")
#     if guess.isdigit():
#         guess = int(guess)
#         guesses += 1
#
#         if guess < lowest_num or guess > highest_num:
#             print("That number is out of range")
#             print(f"Please select a number between {lowest_num} and {highest_num}")
#         elif guess < answer:
#             print("Too low! Try again!")
#         elif guess > answer:
#             print("Too high! Try again")
#         else:
#             print(f"CORRECT! The answer was {answer}")
#             print(f"Number of guesses: {guesses}")
#             is_running = False
#
#     else:
#         print("Invalid guess")
#         print(f"Please select a number between {lowest_num} and {highest_num}")
#
