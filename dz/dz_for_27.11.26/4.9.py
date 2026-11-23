speed_km_h = float(input("Введите первую скорость(в км/ч): "))
speed_m_s = float(input("Введите вторую скорость(в м/с): "))

speed_km_h = speed_km_h * 1000/3600

if speed_km_h > speed_m_s:
    print("Первая скорость больше")
elif speed_km_h < speed_m_s:
    print("Вторая скорость больше")
else:
    print("Скорости равны")