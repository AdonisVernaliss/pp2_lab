import random

a = random.randint(1, 21)


def Guess_the_number():
    print("Hello! What is your name?")
    n = input()
    print("Well, " + n + ", I am thinking of a number between 1 and 20.\nTake a guess.")
    v = int(input())
    c = 0
    for i in range(1, 20):
        c += 1
        if v > a:
            print("Your guess is too big.\nTake a guess.")
            v = int(input())
        elif v < a:
            print("Your guess is too low.\nTake a guess.")
            v = int(input())
        else:
            print("Good job, " + n + "! You guessed my number in", c, "guesses!")
            break


Guess_the_number()
