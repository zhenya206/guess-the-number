def get_guess():
    guess = int(input("Угадайте число: "))
    return guess

def menu():
    print("======================")
    print("      УГАДАЙ ЧИСЛО      ")
    print("======================")
    print("Я загадал число от 1 до 100")
def random_number():
    import random
    return random.randint(1,100)

def big_guess():
    print("Число слишком большое!")

def small_guess():
    print("Число слишком маленькое!!")

def win(attempts):
    print("Поздравляю, Вы угадали!!")
    print(f"Вы угадали за {attempts} попыток!")
    print("1 - Остаться \n 2 - Выйти")

def new_game():
    print("\n======================")
    print("Новая игра!")
    print("Я загадал новое число от 1 до 100")

def continue_game():
    cont = int(input("Вы хотите продолжить: "))
    return cont