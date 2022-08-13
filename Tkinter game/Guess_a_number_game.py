from numpy import random


def guess_game():
    random_number = random.randint(1, 100)
    print(random_number)
    try:
        guess = int(input("Try to guess secret number. Please enter your number between 1 and 100: "))
    except TypeError:
        print("You entered not a number!")
        guess_game()
    counter = 0
    tries = 5
    while counter < 5:
        if guess == random_number:
            print("Congratulations! This is correct number:)")
            break
        elif guess < random_number:
            print("Your number is too low than hidden number.")
            counter += 1
            print(f"You have left {tries - counter} tries.\n")
            if tries - counter == 0:
                print("You loose!")
                break
            guess = int(input("Try again: "))
        elif guess > random_number:
            print("Your number is too high the hidden number.")
            counter += 1
            print(f"You have left {tries - counter} tries.\n")
            if tries - counter == 0:
                print("------You loose!------")
                break
            guess = int(input("Try again: "))


if __name__ == "__main__":
    guess_game()