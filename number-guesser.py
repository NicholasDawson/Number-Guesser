import random

print("-Number Guesser-")
print("")
print("Easy = E | Medium = M | Hard = H")

difficulty = input("Choose difficulty: ")

def Win():
    print("The number was ", randomnum)
    print("You guessed my number in", tries, "tries on", mode, "difficulty!")

def Lose():
    print("You didn't guess my number. The number was", randomnum)


def Easy():
    global mode
    mode = "Easy"
    print("Guess my number between 1-5")
    print("You have 3 Guesses!")
    global tries
    tries = 0
    global randomnum
    randomnum = random.randint(1, 5)
    for e in range(0, 3):
        tries = tries + 1
        guess = int(input("Guess: "))
        if guess is randomnum:
            Win()
            break
        if tries == 3:
            Lose()
            break
        if guess < randomnum:
            print("Higher")
        elif guess > randomnum:
            print("Lower")

def Medium():
    global mode
    mode = "Medium"
    print("Guess my number between 1-10")
    print("You have 3 Guesses!")
    global tries
    tries = 0
    global randomnum
    randomnum = random.randint(1, 10)
    for e in range(0, 3):
        tries = tries + 1
        guess = int(input("Guess: "))
        if guess is randomnum:
            Win()
            break
        if tries == 3:
            Lose()
            break
        if guess < randomnum:
            print("Higher")
        elif guess > randomnum:
            print("Lower")

def Hard():
    global mode
    mode = "Hard"
    print("Guess my number between 1-20")
    print("You have 3 Guesses!")
    global tries
    tries = 0
    global randomnum
    randomnum = random.randint(1, 20)
    for e in range(0, 3):
        tries = tries + 1
        guess = int(input("Guess: "))
        if guess is randomnum:
            Win()
            break
        if tries == 3:
            Lose()
            break
        if guess < randomnum:
            print("Higher")
        elif guess > randomnum:
            print("Lower")

if difficulty in ["e", "E"]:
    Easy()
elif difficulty in ["m", "M"]:
    Medium()
elif difficulty in ["h", "H"]:
    Hard()
else:
    print("Invalid input. Try again.")
