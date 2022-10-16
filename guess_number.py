import random

print("Guess number 1-10")

def guess():
    isGuess = True
    while (isGuess):
        answer = random.randint(1, 10)
        number = int(input("Enter your Answer: "))
        if (answer == number):
            print("Great Job! You WON!!!")
            isGuess = False
            print(answer)
        elif (answer != number):
            print("Bad Guess")
            print(answer)
    
guess()