symbol = input("Введите символ: ")

if (symbol>="a" and symbol<="z") or (symbol>="A" and symbol<="Z"):
    print("Это буква")

    if (symbol>="a" and symbol<="z"):
        print("маленькая")
    else:
        print("большая")

elif symbol>="0" and symbol<="9":
    print("Это цифра")

    if ord(symbol) % 2 == 0:
        print("чётная")
    else:
        print("НЕ чётная")

elif (
    symbol >= "!"
    and symbol <= "/"
    or symbol >= ":"
    and symbol <= "@"
    or symbol >= "["
    and symbol <= "`"
    or symbol >= "{"
    and symbol <= "~"
):
    print("Это спец символ")

else:
    print("Это неопознанный символ")