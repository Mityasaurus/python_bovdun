#Task 1
numbers = (10, 25, 3, 48, 5, 12, 8, 33, 17)
print(numbers)
n = int(input("Введіть число n: "))
result = [num for num in numbers if num < n]
print("Числа з кортежу, менші за", n, ":", result)

#Task 2
strings = ("apple", "banana", "cherry")
print(strings)
result = ", ".join(strings)
print(result)

#Task 3
library = {
    "1984": ("George Orwell", 1949, 328),
    "To Kill a Mockingbird": ("Harper Lee", 1960, 281),
    "Pride and Prejudice": ("Jane Austen", 1813, 279)
}

book_name = input("Enter the name of the book: ")
print(book_name)

if book_name in library:
    author, year, pages = library[book_name]
    print(f"Author: {author}")
    print(f"Year: {year}")
    print(f"Pages: {pages}")
else:
    print("Sorry, this book is not available in the library.")

#Task 4
students = {
    "Smith": ("John", 20, "Computer Science"),
    "Johnson": ("Emily", 22, "Mathematics"),
    "Williams": ("Michael", 19, "Physics")
}

last_name = input("Enter the student's last name: ")
print(f"Last name: {last_name}")

if last_name in students:
    first_name, age, major = students[last_name]
    print(f"First Name: {first_name}")
    print(f"Age: {age}")
    print(f"Major: {major}")
else:
    print("Sorry, no information available for this student.")

#Task 5
phonebook = {
    "John": ("123-456-789", "987-654-321"),
    "Emily": ("555-666-777",),
    "Michael": ("222-333-444", "333-444-555")
}

def add_phone_number(contact_name, new_number):
    if contact_name in phonebook:
        phonebook[contact_name] = phonebook[contact_name] + (new_number,)
    else:
        phonebook[contact_name] = (new_number,)

add_phone_number("John", "111-222-333")
add_phone_number("Alice", "444-555-666")

for contact, numbers in phonebook.items():
    print(f"{contact}: {', '.join(numbers)}")