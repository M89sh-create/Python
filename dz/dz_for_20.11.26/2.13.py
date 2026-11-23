og_number = 0
reverse_number = 0

number1 = 0
number2 = 0
number3 = 0

og_number = int(input("Введите трёхзначное число: "))

number1 = og_number//100
number2 = (og_number//10)%10
number3 = og_number%10

reverse_number = number3*100 + number2*10 + number1

print(f"Ваше число, если читать его справа налево: {reverse_number}")