#2. Guess a number - 

import random

num = random.randint(1, 100)

guess = None


while guess != num:

    guess = input("guess a number between 1 and 100: ")

    guess = int(guess)

    if guess == num:

        print("congratulations! you won!")

        break

    elif guess > num:

        print("Nope, sorry. your number is greater than the actual number")

    else:

        print("Nope, sorry. your number is smaller than the actual number")