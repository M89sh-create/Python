n1 = int(input("Введите первое число: "))
n2 = int(input("Введите второе число: "))
n3 = int(input("Введите третье число: "))

min_number = 0
max_number = 0
average_number = 0

min_number = min(n1, n2, n3)
max_number = max(n1, n2, n3)

if n1 > min_number and n1 < max_number:
    average_number = n1
elif n2 > min_number and n2 < max_number:
    average_number = n2
else:
    average_number = n3


print("\n=================\n")

print(f"Самое большое число: {max_number}")
print(f"Самое маленькое число: {min_number}")
print(f"Среднее число: {average_number}")