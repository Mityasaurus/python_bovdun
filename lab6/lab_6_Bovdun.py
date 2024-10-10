#Task 1
def is_year_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end=" ")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

#Task 2
def days_in_month(year, month):
    if month < 1 or month > 12:
        return None

    days = [31, 29 if is_year_leap(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days[month - 1]

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]

for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end=" ")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

#Task 3
def day_of_year(year, month, day):
    if days_in_month(year, month) is None or day < 1 or day > days_in_month(year, month):
        return None
    total_days = sum(days_in_month(year, m) for m in range(1, month)) + day
    return total_days

test_years = [2000, 1900, 2016, 2023, 2023, 2023]
test_months = [12, 2, 1, 2, 4, 2]
test_days = [31, 28, 15, 29, 31, 28]
test_results = [366, 59, 15, None, None, 59]

for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    day = test_days[i]
    print(f"{yr}, {mo}, {day} ->", end=" ")
    result = day_of_year(yr, mo, day)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

#Task 4
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()

#Task 5
def liters_100km_to_miles_gallon(liters):
    miles_per_km = 1 / 1.609344
    gallons_per_liter = 1 / 3.785411784
    return 100 * miles_per_km / (liters * gallons_per_liter)

def miles_gallon_to_liters_100km(miles):
    km_per_mile = 1.609344
    liters_per_gallon = 3.785411784
    return 100 / (miles * km_per_mile / liters_per_gallon)

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.0))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

#Task 6
def is_a_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

test_sides = [
    (3, 4, 5),
    (1, 1, 2),
    (5, 5, 5),
    (10, 2, 7),
    (6, 8, 10),
    (1, 2, 3)
]

test_results = [True, False, True, False, True, False]

for i in range(len(test_sides)):
    a, b, c = test_sides[i]
    print(f"{a}, {b}, {c} ->", end=" ")
    result = is_a_triangle(a, b, c)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

#Task 7
def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False

    sides = sorted([a, b, c])

    return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2


test_triangles = [
    (3, 4, 5),
    (5, 12, 13),
    (1, 1, 1),
    (2, 2, 3),
    (8, 15, 17),
    (7, 24, 25)
]

test_results = [True, True, False, False, True, True]

for i in range(len(test_triangles)):
    a, b, c = test_triangles[i]
    print(f"{a}, {b}, {c} ->", end=" ")
    result = is_a_right_triangle(a, b, c)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")