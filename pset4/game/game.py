import random

while True:
    try:
        level = int(input("Level: "))
        if level >= 1:
            break
    except ValueError:
        print("Please enter a positive integer.")

random_number = random.randint(1, level)

while True:
    try:
        player_guess = int(input("Guess: "))
        if random_number > player_guess:
            print("Too small!")
        elif random_number < player_guess:
            print("Too large!")
        elif random_number == player_guess:
            print("Just right!")
            break
    except ValueError:
        print("Please enter a number.")