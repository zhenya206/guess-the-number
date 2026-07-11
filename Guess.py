import random

number = random.randint(1,100)
attempts = 0
answer = 0
print("======================")
print("      УГАДАЙ ЧИСЛО      ")
print("======================")
print("Я загадал число от 1 до 100")
while answer != number:
    answer = int(input("Угадайте число: "))
    attempts += 1
    if answer > number:
        print("Число слишком большое!")


    elif answer < number:
        print("Число слишком маленькое!!")


    else:
        print("Поздравляю, Вы угадали!!")
        print(f"Вы угадали за {attempts} попыток!")
        print("1 - Остаться \n 2 - Выйти")
        cont = int(input("Вы хотите продолжить: "))
        if cont == 1:
            number = random.randint(1, 100)
            attempts = 0
            answer = 0
            print("\n======================")
            print("Новая игра!")
            print("Я загадал новое число от 1 до 100")


        else:
            break




