print("Давайте выведем на экран приветствие!\nНапример что нибудь кроме 'Hello World'")
user_input = input("Попробуйте, у Вас получится: ")

if user_input == "Hello World" or user_input == "hello world":
    while user_input == "Hello World" or user_input == "hello world":
        print("Ну нееет, давай попробуем еще раз, у нас получится!")
        user_input = input("Попробуйте, у Вас получится: ")
    print(f"{user_input}\nУра! У нас получилось!")

print(f"{user_input}\nУра! У нас получилось!")

user_number = int(input("А какое твое любимое число?: "))
print(F"Здорово! {user_number} и мое любимое число.")