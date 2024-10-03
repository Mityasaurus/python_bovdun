#Task 1
hat_list = [1, 2, 3, 4, 5]

hat_list[2] = int(input("Введіть нове число для заміни середнього елемента списку: "))
hat_list.pop()
print("Довжина списку після змін:", len(hat_list))
print(hat_list)

#Task 2
arr = list(map(int, input("Введіть елементи списку через пробіл: ").split()))

n = len(arr)
for i in range(n - 1):
    swapped = False
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True
    if not swapped:
        break

print("Відсортований список:", arr)

#Task 3
my_list = list(map(int, input("Введіть елементи списку через пробіл: ").split()))
unique_list = []

for num in my_list:
    if num not in unique_list:
        unique_list.append(num)

print("Список лише з унікальними елементами:")
print(unique_list)

#Task 4
chessboard = [["_" for _ in range(8)] for _ in range(8)]
chessboard[0][0] = chessboard[0][7] = chessboard[7][0] = chessboard[7][7] = "R"
for row in chessboard:
    print(" ".join(row))