import random

def guess_number():
    # Загадываем случайное число от 1 до 100
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Привет! Давай сыграем в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. Попробуй угадать.")

    while True:
        try:
            guess = int(input("Введи свой вариант: "))
            attempts += 1

            if guess < secret_number:
                print("Слишком маленькое число. Попробуй ещё раз.")
            elif guess > secret_number:
                print("Слишком большое число. Попробуй ещё раз.")
            else:
                print(f"Поздравляю! Ты угадал число {secret_number} за {attempts} попыток.")
                break
        except ValueError:
            print("Неверный ввод. Введи целое число.")

# Запускаем игру
guess_number()
