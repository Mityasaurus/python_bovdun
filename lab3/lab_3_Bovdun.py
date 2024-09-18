#Task 1
pi = 3.141592653589793
e = 2.718281828459045

x = float(input("Введіть значення x: "))
mu = float(input("Введіть значення середнього (mu): "))
sigma = float(input("Введіть значення стандартного відхилення (sigma): "))

sqrt_2pi = (2 * pi) ** 0.5
coefficient = 1 / (sigma * sqrt_2pi)

exponent = e ** (-((x - mu) ** 2) / (2 * sigma ** 2))

result = coefficient * exponent

print(f"Значення функції Гауса для x = {x}, mu = {mu}, sigma = {sigma}: {result}")

#Task 2
john = 3
mary = 5
adam = 6

print(john, mary, adam, sep=", ")

total_apples = john + mary + adam

print(total_apples)
print("Загальна кількість яблук:", total_apples)

#Task 3
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

#Task 4
x = 1
x = float(x)
y = 3 * (x ** 3) - 2 * (x ** 2) + (3 ** x) - 1
print("y =", y)

#Task 5
# This program computes the number of seconds in a given number of hours.

hours = 2  # Number of hours to convert
seconds_per_hour = 3600  # Number of seconds in 1 hour

print("Hours:", hours)  # Display the number of hours
print("Seconds in given hours:", hours * seconds_per_hour)  # Calculate and display the total number of seconds

# Printing "Goodbye"
print("Goodbye")

#Task 6
a = float(input("Enter the first number (a): "))

b = float(input("Enter the second number (b): "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

print("\nThat's all, folks!")

#Task 7
x = float(input("Enter value for x: "))

inner_most = 1 / x
second_inner = 1 / (x + inner_most)
third_inner = 1 / (x + second_inner)
fourth_inner = 1 / (x + third_inner)

y = 1 / (x + fourth_inner)

print("y =", y)

#Task 8
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

total_minutes = hour * 60 + mins + dura

end_hour = (total_minutes // 60) % 24
end_minute = total_minutes % 60

print(f"Event ends at {end_hour}:{end_minute}")