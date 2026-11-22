import random

comp_number = random.randint(1, 100)

is_run = True

count_tries = 0

while is_run == True:
    count_tries += 1

    user_number = int(input("Введите число от 1 до 100: "))

    if user_number > comp_number:
        print("Введите поменьше")

    if user_number < comp_number:
        print("Введите побольше")

    if user_number == comp_number:
        print("Ураааа вы угадали!!")
        is_run = False

print(f"Вы потратили на это {count_tries} попыток")
