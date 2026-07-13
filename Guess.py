import func as f


number = f.random_number()
attempts = 0
f.menu()
while True:
    user = f.get_guess()
    attempts += 1
    if user > number:
        f.big_guess()
    elif user < number:
        f.small_guess()
    else:
        f.win(attempts)
        cont = f.continue_game()

        if cont == 1:
            attempts = 0
            number = f.random_number()
            f.new_game()
        else:
            break




