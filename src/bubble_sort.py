def bubble_sort(arg):
    n = len(arg)
    for i in range(n):
        for k in range(0, n - i - 1):
            if arg[k] > arg[k + 1]:
                arg[k], arg[k + 1] = arg[k + 1], arg[k]
    return arg


numbers_input = input("Введите числа (через пробел): ")

parts = numbers_input.split()
numbers = []

for part in parts:
    number = int(part)  
    numbers.append(number)

sorted_numbers = bubble_sort(numbers)
print("Отсортированный список:", sorted_numbers)