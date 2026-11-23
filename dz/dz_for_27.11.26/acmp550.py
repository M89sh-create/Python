year = int(input())

if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print("12/09/" + f"{year:04}")
else:
    print("13/09/" + f"{year:04}")