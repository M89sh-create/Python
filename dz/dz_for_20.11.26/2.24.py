first_number = 0
second_number = 237
digit3 = 0

digit3 = second_number//100

second_number -= digit3*100
second_number *= 10
second_number += digit3

first_number = second_number

print(f"Исходное число x: {first_number}")