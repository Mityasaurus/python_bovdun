#Example 1
def ispalindrom(text):
    text = text.replace(" ", "").lower()
    if text == text[::-1]:
        print("It's a palindrom")
    else:
        print("It's not a palindrom")

text = input("Введіть текст:")
print(text)
ispalindrom(text)

text = input("Введіть текст:")
print(text)
ispalindrom(text)

#Example 2
# Перевірка на анаграму

text1 = input("Введіть перше слово:")
print(text1)
text2 = input("Введіть друге слово:")
print(text2)

text1 = list(text1.replace(" ", "").lower())
text2 = list(text2.replace(" ", "").lower())

if sorted(text1) == sorted(text2):
    print("Анаграми")
else:
    print("Не анаграми")

#Example 3
# Обчислює число "життя": суму цифр повної дати народження
date = input("Введіть дату народження у форматі YYYYMMDD:")
print(date)

while True:
    sum = 0
    for simbol in date:
        sum += int(simbol)

    date = str(sum)

    if len(date) == 1:
        break

print(sum)

#Task 1
def is_hidden(word, combination):
    word = word.lower()
    combination = combination.lower()
    index = 0

    for char in combination:
        if char == word[index]:
            index += 1
        if index == len(word):
            return "Yes"

    return "No"


word = input("Введіть слово: ")
print(word)
combination = input("Введіть комбінацію символів: ")
print(combination)
print(is_hidden(word, combination))

#Example 4
while True:
    try:
        number = int(input(" Введіть ціле число: "))
        print(number/2)
        break
    except:
        print("Введене значення не є допустимим числом. Повторіть спробу...")

#Task 2
def calculate_life_number(date):
    digits = ''.join(filter(str.isdigit, date))

    digit_sum = sum(int(d) for d in digits)

    while digit_sum > 9:
        digit_sum = sum(int(d) for d in str(digit_sum))

    return digit_sum


while True:
    try:
        date = input("Введіть дату народження у форматі РРРРММДД, РРРРДДММ або ММДДРРРР: ")

        if len(date) < 8:
            raise ValueError("Дата має бути мінімум 8 символів.")

        life_number = calculate_life_number(date)
        print("Цифра життя для дати {}: {}".format(date, life_number))
        break
    except ValueError as ve:
        print(f"Помилка: {ve}. Спробуйте ще раз.")
    except Exception as e:
        print(f"Невідома помилка: {e}. Спробуйте ще раз.")

#Task 3
def get_integer_input(prompt, min_value, max_value):
    while True:
        user_input = input(prompt)

        try:
            value = int(user_input)
        except ValueError:
            print("Error: wrong input")
            continue

        if value < min_value or value > max_value:
            print(f"Error: the value is not within permitted range ({min_value}..{max_value})")
            continue

        return value


result = get_integer_input("Введіть ціле число: ", 1, 10)
print(f"Ви ввели допустиме число: {result}")