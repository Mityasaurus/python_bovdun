#Example 1
# Написати метод аналогічний split()
def mysplit(string):
    if not string or string.isspace():
        return []

    words = []
    word = ""
    for char in string:
        if char != ' ':
            word += char
        elif word:
            words.append(word)
            word = ""

    if word:
        words.append(word)

    return words

# I варінат (некрасивий, але, можливо, оптимальніший, ніж ІІ)
# def mysplit(string):
#     string = string.lstrip() # метод strip() не змінює об'єкт, а створює копію!

#     list_split = []

#     if string.isspace() or string == "": # якщо рядок пустий, або з одних пробілів
#         return list_split

#     if string.find(' ') == -1: # якщо з одного слова
#         list_split.append(string)
#         return list_split

#     fnd_1 = 0
#     fnd_2 = string.find(' ')

#     while fnd_2 != -1:
#         list_split.append(string[fnd_1:fnd_2])
#         fnd_1 = fnd_2
#         fnd_2 = string.find(' ', fnd_2 + 1)

#     return list_split

# ІІ варіант (красивий, але не факт, що оптимальний)

# def mysplit(string):
#     list_split = []
#     word = ""
#     for char in string:
#         if char == " ":
#             if word:
#                 list_split.append(word)
#             word = ""
#         else:
#             word += char
#     if word:
#         list_split.append(word)
#     return list_split


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

#Example 2
# Тут має бути Ваш код
# number_input = input('Введіть ціле число: ')
# number_list = [str(i) for i in range(0, 10)]
number_dict = {'1' : ('  #', '  #', '  #', '  #', '  #'),
               '2' : ('###', '  #', '###', '#  ', '###'),
               '3' : ('###', '  #', '###', '  #', '###'),
               '4' : ('# #', '# #', '###', '  #', '  #'),
               '5' : ('###', '#  ', '###', '  #', '###'),
               '6' : ('###', '#  ', '###', '# #', '###'),
               '7' : ('###', '  #', '  #', '  #', '  #'),
               '8' : ('###', '# #', '###', '# #', '###'),
               '9' : ('###', '# #', '###', '  #', '###'),
               '0' : ('###', '# #', '# #', '# #', '###')
               }
def display_number(num):
    if num < 0:
        print("Число має бути невід'ємним.")
        return

    num_str = str(num)

    for level in range(5):
        for symbol in num_str:
            print(number_dict[symbol][level], end=' ')
        print()

display_number(12345)

#Example 3
# Caesar cipher.
text = input("Enter your message: ")
print(text)
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)

#Example 4
# Caesar cipher - decrypting a message.
cipher = input('Enter your cryptogram: ')
print(cipher)
text = ''
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)

#Task 1
while True:
    try:
        shift = int(input("Enter shift value (1-25): "))
        if 1 <= shift <= 25:
            break
        else:
            print("Shift value must be between 1 and 25.")
    except ValueError:
        print("Invalid input. Please enter an integer between 1 and 25.")

print("Shift: ", shift)
text = input("Enter your message: ")
print(text)
cipher = ''

for char in text:
    if char.isalpha():
        start = ord('A') if char.isupper() else ord('a')
        code = start + (ord(char) - start + shift) % 26
        cipher += chr(code)
    else:
        cipher += char

print("Ciphered text:", cipher)