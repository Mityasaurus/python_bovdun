#Task 1
n = 100
print(n >= 100)
n = 55
print(n >= 100)

#Task 2
a = 2.48
b = 1.51
if a > b:
    print(a)
else:
    print(b)

#Task 3
plant = input()
print(plant)
if plant == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif plant == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print(f"Spathiphyllum! Not {plant}!")

#Task 4
income = float(input("Enter the annual income: "))
print("Income: ", income)

if income <= 85528:
    tax = income * 0.18 - 556.02
else:
    tax = 14839.02 + (income - 85528) * 0.32

tax = round(tax, 0)

if tax < 0:
    tax = 0

print("The tax is:", tax, "thalers")

#Task 5
year = int(input("Enter a year: "))

if year < 1582:
    print("Not within the Gregorian calendar period")
elif year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Common year")

#Task 6
secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

while True:
    guess = int(input("Enter your guess: "))
    print("Guess: ", guess)
    if guess == secret_number:
        print(
        """
        +-----------------------------+
        | Молодець, магле!             |
        | Тепер ти вільний!            |
        +-----------------------------+
        """)
        break
    else:
        print(
        """
        +-----------------------------+
        | Ха-ха!                      |
        | Ви застрягли у моїй петлі!  |
        +-----------------------------+
        """)

#Task 7
import time

for i in range(1, 6):
    print(f"{i} Mississippi")
    time.sleep(1)

print("Ready or not, here I come!")

#Task 8
while True:
    user_input = input("Please enter a word: ")
    if user_input == "chupacabra":
        print("You've successfully left the loop.")
        break

#Task 9
user_word = input("Please enter a word: ")
print(user_word)
user_word = user_word.upper()
for letter in user_word:
    if letter in "AEIOU":
        continue
    print(letter)

#Task 10
user_word = input("Please enter a word: ")
print(user_word)
user_word = user_word.upper()
word_without_vowels = ""

for letter in user_word:
    if letter in "AEIOU":
        continue
    word_without_vowels += letter

print(word_without_vowels)

#Task 11
total_blocks = int(input("Enter the number of blocks: "))
height = 0
blocks_used = 0

while blocks_used + (height + 1) <= total_blocks:
    height += 1
    blocks_used += height

print(f"The height of the pyramid is: {height}")

#Task 12
c0 = int(input("Enter a natural number: "))
steps = 0

while c0 != 1:
    print(c0)
    if c0 % 2 == 0:
        c0 //= 2
    else:
        c0 = 3 * c0 + 1
    steps += 1

print(c0)
print(f"Total steps: {steps}")