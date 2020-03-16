print("'Преобразователь времени!'")
user_time = int(input("Введите количество секунд: "))

if user_time < 0:
    user_time = int(input("Увы, мы не конвертируем упущеное время, введите положительное число: "))

h = user_time // 60 // 60
min = user_time // 60 % 60
sec = user_time - (h * 3600 + min * 60)

if h < 10 and min < 10 and sec < 10:
    print(f"Ваше конвертированое время: 0{h}:0{min}:0{sec}")
elif h < 10 and min < 10:
    print(f"Ваше конвертированое время: 0{h}:0{min}:{sec}")
elif h < 10 and sec < 10:
    print(f"Ваше конвертированое время: 0{h}:{min}:0{sec}")
elif min < 10 and sec < 10:
    print(f"Ваше конвертированое время: 0{h}:{min}:0{sec}")
elif h < 10:
    print(f"Ваше конвертированое время: 0{h}:{min}:{sec}")
elif min < 10:
    print(f"Ваше конвертированое время: {h}:0{min}:{sec}")
elif sec < 10:
    print(f"Ваше конвертированое время: {h}:{min}:0{sec}")
else:
    print(f"Ваше конвертированое время: {h}:{min}:{sec}")
