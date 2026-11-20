og_number = 0

number1 = 0
number2 = 0
number3 = 0
number4 = 0

sum = 0
product = 0

og_number = int(input("Введите четырёхзначное число: "))

number1 = og_number//1000
number2 = (og_number//100)%10
number3 = (og_number//10)%10
number4 = og_number%10

sum = number1 + number2 + number3 + number4
product = number1 * number2 * number3 * number4

print(f"Сумма цифр вашего числа: {sum}")
print(f"Произведение цифр вашего числа: {product}")