import random
from time import sleep
number = random.randint(1, 100)

print("Итак, загадано число от 1 до 100. Попробуй угадать если сможешь!")

attemps = 0

while True:

    guess = int(input("Ты думаешь это число: "))

    attemps += 1

    if guess < number:
        print("Маловато будет!")
    elif guess > number:
        print("Многовато будет!")
    else:
        print("Ты угадал!")
        print(f"Тебе понадобилось {attemps} попыток.")
        print("Хочешь сыграть ещё раз? (да/нет)")
        answer = input().upper()
        if answer == "ДА":
            attemps = 0
        elif answer == "НЕТ":
            print("Ещё свидимся!")
            break
        else:
            print("Моя твоя не понимать! Может попробуешь ещё раз? Сыграем ещё раз (да/нет)")
            answer = input().upper()
            if answer == "ДА":
                attemps = 0
            elif answer == "НЕТ":
                print("Ещё свидимся!")
                break
            else:
                print("Ой, да иди ты!")
                sleep(0.5)
                break