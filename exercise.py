# Variable = A container for a value (string, integer, float, boolean)
#            A variable behaves as if it was the value it contains

# Strings
first_name = "Jeremy"
food = "Noodles"
email = "jeremy2388@gmail.com"
# print(f"Hello {first_name}")
# print(f"You like {food}")
# print(f"You're email is: {email}")

# Integers
age = 21
quantity = 3
num_of_students = 30
# print(f"You're {age} years old")
# print(f"You are buying {quantity} items")
# print(f"Your class has {num_of_students} students")

# Float
price = 10.99
gpa = 3.7
distance = 5.5
# print(f"The price is $: {price}")
# print(f"Your gpa is {gpa}")
# print(f"You ran {distance} km")

# Boolean
is_student = True
for_sale = False
is_online = True
# if is_student:
#     print("You are a student")
# else:
#     print("You are not a student")
#
# if for_sale:
#     print("That item is for sale")
# else:
#     print("That item is NOT available")
#
# if is_online:
#     print("You're online")
# else:
#     print("You're offline")

# Typecasting = the process of converting a variable from one data type to another str(), int(), float(), bool()

name = ""
age = 21
gpa = 3.9
is_student = True

# print(type(age))
# age = float(age)
age = str(age)
age += "1"

# name = bool(name)
# print(name)

# input() function: a function that prompts the user to enter data
#                   Returns the entered data as a string

# input("Who the best player?: ")
# name = "jeremy"
# print(f"well choice {name}!")

# name = input("What is your name?: ")
# age = int(input("How old are you?: "))
# age = age + 1
# print(f"Hello {name}!")
# print("HAPPY BIRTHDAY!")
# print(f"You are {age} years old innit")

# length = float(input("Enter the length: "))
# width = int(input("Enter the width: "))
# area = length * width
#
# print(f"The answer to the area: {area}cm^2")

# item = input("What item would you like to buy?: ")
# price = float(input("What is the price?: "))
# quantity = int(input("How many would you like?: "))
# total = price * quantity
#
# print(f"You have bought {quantity} x {item}/s")
# print(f"You're total is: ${total}")

# Exercise
# Madlibs game
# Word game where you create a story
# By filling in blanks with random words

# adjective1 = input("Enter and adjective (description): ")
# noun1 = input("Enter a noun (person, place, thing): ")
# adjective2 = input("Enter an adjective (description): ")
# verb1 = input("Enter a verb ending with 'ing': ")
# adjective3 = input("Enter an adjective (description): ")
#
# print(f"Today i went to {adjective1} zoo.")
# print(f"In an exhibit, I saw a {noun1}")
# print(f"{noun1} was {adjective2} and {verb1}")
# print(f"I was {adjective3}!")

friends = 10

# friends = friends + 1
# friends += 1
# friends = friends - 2
# friends -= 2
# friends = friends * 3
# friends *= 3
# friends = friends / 2
# friends /= 2
# friends = friends ** 2
# friends **= 2
# remainder = friends % 2
# print(remainder)

x = 3.67
y = 4
z = 5

# result = round(x)
# result = abs(y)
# result = pow(2, 2)
# result = max(x, y, z)
# result = min(x, y, z)
# print(result)

import math
# x = 9.9
# print(math.pi)
# print(math.cos(24))
# print(math.e)
# result = math.sqrt(x)
# result = math.ceil(x)
# result = math.floor(x)
# print(result)

# radius = float(input("Enter the radius of the circle: "))
# circumference = 2 * math.pi * radius
#
# print(f"The circumference is: {round(circumference, 3)}")

# radius = float(input("Enter the radius of a circle: "))
# area = math.pi * pow(radius, 2)
# print(f"The area of the circle is: {round(area)}cm^2")

# a = float(input("Enter side A: "))
# b = float(input("Enter side B: "))
# c = int(math.sqrt(pow(a, 2) + pow(b, 2)))
#
# print(f"Side c = {c}")


# if = Do some code onli IF some condition is True
#      Else do something else
#
# age = int(input("Enter your age: "))
#
# if age >= 100:
#     print("You are mentalll!")
# elif age >= 18:
#     print("You are now sign up!")
# elif age < 0:
#     print("You haven't born yet!")
# else:
#     print("You must be 18+ to sign up!")

# response = input("Would you like food? (Y/N): ")
#
# if response == "Y":
#     print("Have some manner you are doesn't have manner!!")
# elif response == "N":
#     print("You will be hungry don't be silly!!")
# else:
#     print("No food for you pal!")

# name = input("Enter your name: ")
#
# if name == "":
#     print("You did not type in your name!")
# elif name == "123":
#     print("Idiott type your real name!!!!")
# else:
#     print(f"Hello {name}")

# online = True
#
# if online:
#     print("The user is online")
# else:
#     print("The user is offline")

# # Python Calculator
# operator = input("Enter an operator (+ - * /): ")
# num1 = float(input("Enter the 1st number: "))
# num2 = float(input("Enter the 2nd number: "))
#
# if operator == "+":
#     result = num1 + num2
#     print(result)
# elif operator == "-":
#     result = num1 - num2
#     print(result)
# elif operator == "*":
#     result = num1 * num2
#     print(result)
# elif operator == "/":
#     result = num1 / num2
#     print(round(result, 2)) # Two number after the decimal
# else:
#     print(f"{operator} is not a valid operator!!!")


# # Python weight converter
# weight = float(input("Enter your weight: "))
# unit = input("Kilogram or Pounds? (K or L): ")
#
# if unit == "K":
#     weight = weight * 2.205
#     unit = "Lbs"
#     print(f"You're weight is: {round(weight, 1)} {unit}")
# elif unit == "L":
#     weight = weight / 2.205
#     unit = "Kgs"
#     print(f"You're weight is: {round(weight, 1)} {unit}")
# else:
#     print(f"{unit} was not valid!")

# unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
# temp = float(input("Enter the temperature: "))
#
# if unit == "C":
#     temp = round((9 * temp) / 5 + 32, 1)
#     print(f"The temperature in Fahrenheit is: {temp}oF")
# elif unit == "F":
#     temp = round((temp -32) * 5 / 9, 1)
#     print(f"The temperature in Celcius is: {temp}oC")
# else:
#     print(f"{unit} is invalid unit of measurement")

# Logical operators = evaluate multiple conditions (or, and, not)
#                     or = at least one condition must be True
#                     and = both conditions must be True
#                     not = inverts the condition (not False, not True)
#
# temp = 25
# is_raining = True
#
# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is still scheduled")

# temp = -1
# is_sunny = False
#
# if temp >= 28 and is_sunny:
#     print("It is HOT oustide")
#     print("It is SUNNY")
# elif temp <= 0 and not is_sunny:
#     print("It is COLD outside")
#     print("It is SUNNY")
# elif 28 > temp > 0 and is_sunny:
#     print("It is WARM oustide")
#     print("It is SUNNY")

# Conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on a condition
#                          X if condition else Y

# num = 5
# a = 6
# b = 7
# age = 17
# temperature = 20
# user_role = "admin"
# # print("Positive" if num > 0 else "Negative")
# # result = "Even" if num % 2 == 0 else "ODD"
# # max_num = a if a > b else b
# # min_num = a if a < b else b
# # status = "Adult" if age >= 18 else "Child"
# # weather = "HOT" if temperature > 20 else "COLD"
# access_level = "Full access" if user_role == "admin" else "Limited Access"
# print(access_level)

# name = input("Enter your fulll name: ")
# phone_number = input("Enter your phone #: ")
# result = len(name)
# result = name.find("J")
# result = name.rfind("e")
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
# result = name.isalpha()
# phone_number = phone_number.count("-", " ")
# phone_number = phone_number.replace("-", " ")
# print(phone_number)
# print(help(str))

# username = input("Enter a username: ")
#
# if len(username) > 12:
#     print("Your username can't be more than 12 characters")
# elif not username.find(" ") == -1:
#     print("Your username can't contain spaces")
# elif not username.isalpha():
#     print("Your username can't contain numbers")
# else:
#     print(f"Welcome {username}")

# Indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

# credit_number = "1234-4567-7859-3448"
# last_digit = credit_number[-4:]
# print(f"XXXX-XXXX-XXXX-{last_digit}")
# print(credit_number[:5])
# print(credit_number[5:10])
# print(credit_number[-2:])
# print(credit_number[::2])
# # print(credit_number[::3])
# credit_number = credit_number[::-1]
# print(credit_number)

# format specifiers = {value:flags} format a value based on what flags are inserted

price1 = 3000.14159
price2 = -9870.65
price3 =1200.34

# print(f"Price 1 is ${price1:1}")
# print(f"Price 2 is ${price2:.3f}")
# print(f"Price 3 is ${price3:.5f}")
# print(f"price 1 is ${price1:^10}")
# print(f"Price 1 is ${price1:,}")
# print(f"Price 2 is ${price2:,}")
# print(f"Price 3 is ${price3:,}")

# print(f"price 1 is ${price1:+,.2f}")

# while loop = execute some code WHILE some condition remains true

# name = input("Enter your name: ")
#
# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name lad: ")
# print(f"Hello {name}")

# age = int(input("Enter your age: "))
#
# while age < 0:
#     print("Age can't be negative pall!")
#     age = int(input("Enter your real age pall: "))
#
# print(f"You are {age} years old mateee")

# food = input("Enter a food you like (q to quit): ")
#
# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter another food you like (q to quit): ")
#
# print("bye enjoyy your food")

# num = int(input("Enter a # between 1 - 10: "))
#
# while num < 1 or num > 10:
#     print(f"{num} is not valid")
#     num = int(input("Enter a # between 1 - 10: "))
#
# print(f"Your number is {num}")

# Python compound interest calculator

# principle = 0
# rate = 0
# time = 0
#
# while principle <= 0: # can be while True
#     principle = float(input("Enter the principle amount: "))
#     if principle < 0:
#         print("principle can't be less than or equal to zero")
# # else: break
# while rate <= 0: # can be while True
#     rate = float(input("Enter the interest rate: "))
#     if rate <= 0:
#         print("Interest rate can't be less than or equal to zero")
# # else: break
# while time <= 0: # can be while true
#     time = float(input("Enter the time in years: "))
#     if time <= 0:
#         print("Time can't be less than or equal to zero")
# # else:break
# total = principle * pow((1 + rate / 100), time)
# print(f"Balance after {time} year/s: ${total:.2f}")

# for loops = execute a block of code a fixed number of times.
#             You can iterate over a range, string, sequence, etc.

# for x in reversed(range(1, 11)):
#     print(x)
# barca = "VISCA BARCA VISCA CATALUNYA!!!"
# print(f"GAME ONNNNNN! {barca}")

# credit_card = "123-4332-4484-38273"

# for x in credit_card:
#     print(x)

# i = 1
# while i <= 11:
#     if i == 8:
#         i += 1
#         continue  #
#     print(i)
#     i += 1


# for x in range (1, 21):
#     if x == 13:
#         continue
#     else:
#         print(x)

import time

# my_time = int(input("Enter the time in seconds: "))

# for x in (range(my_time, 0, -1)):
#     seconds = x % 60
#     minutes = int(x / 60) % 60
#     hours = int(x / 3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)
#
# print("TIME'S UP!")

# import time
#
# my_time = int(input("Enter the time in seconds: "))
#
# for x in range(my_time, 0, -1):
#     days = int(x / 86400)  # 1 hari = 86400 detik
#     hours = int((x % 86400) / 3600)  # Sisa detik setelah menghitung hari, lalu konversi ke jam
#     minutes = int((x % 3600) / 60)  # Sisa detik setelah menghitung jam, lalu konversi ke menit
#     seconds = x % 60  # Sisa detik setelah menghitung menit
#     print(f"{days:02}:{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)
#
# print("TIME'S UP!")

# nested loop = A loop within another loop (outer, inner)
#               outer loop:
#                   inner loop:

# rows = int(input("Enter the # of rows: "))
# columns = int(input("Enter the # of columns: "))
# symbol = (input("Enter a symbol to use: "))
#
# for x in range(rows):
#     for y in range(columns):
#         print(symbol, end="")
#     print()


# collection = single "variable used to store multiple values"
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK. No duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. Faster

# fruits = ["apple", "orange", "orange", "banana", "coconut"]
# print(fruits[::-1])
# fruits.reverse()
# print(fruits)
# for fruit in fruits:
#     print(fruit)
# print(len(fruits))
# print("app" in fruits)
# fruits[0] = "pineaple"
# fruits.append("Cucumber")
# fruits.remove("orange")
# fruits.insert(0, "Grape")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("apple"))
# print(fruits.count("orange"))
# print(fruits)

# i = 0
# while i < len(fruits):
#     print(fruits[i])
#     i += 1

# Set = {} unordered and immutable but add/remove OK. No duplicates
# fruits = {"apple","orange", "banana", "coconut"}
# print(dir(fruits))
# print(len(fruits))
# print("grape" in fruits)
# fruits.add("grape")
# fruits.remove("grape")
# fruits.pop()
# fruits.clear()
# fruits.add("strawberry")
# print(fruits)


# Tuple = () ordered and unchangeable. Duplicates OK. faster
# fruits = ("apple", "orange", "banana", "coconut", "coconut")
# # print(fruits.index("banana"))
# print(fruits.count("coconut"))
# for fruit in fruits:
#     print(fruit)
# print(fruits)
# print(len(fruits))

# Shopping cart program
# foods = []
# prices = []
# total = 0
#
# while True:
#     food = input("Enter a food to buy (q to quit): ")
#     if food.lower() == "q":
#         print("see you again byebyeee!")
#         break
#     else:
#         price = float(input(f"Enter the price of a {food}: $"))
#         foods.append(food)
#         prices.append(price)
# print("------ YOUR CART -------")
#
# # Cara pertama
# for food in foods:
#     print(food, end=" ")
#
# for price in prices:
#     total += price
# print()
# print(f"Your total is: ${total}")

# print(", ".join(foods) + ".")













































