# A Hangman game by atopheim
# Written in python 3.6 - 25.09.2017

import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

print("Welcome a hangman type game by atopheim")
print("")

correctText = input("Secret word: ")
tries = int(input("Number of tries: "))
clearConsole()

currentText = "*" * len(correctText)
print(currentText)
def test(x):
    y=""
    for i in range(len(correctText)):
        if correctText[i] == x:
            y += x
        else:
            y+=currentText[i]
    return y
x=len(correctText)

for i in range(x):
    guess = input("Guess: ")
    if guess in correctText and len(guess)<2:
        currentText=test(guess)
        print("Correct", currentText)
        if currentText == correctText:
            print("Congratulations, you WON!")
            break
    elif guess not in correctText and len(guess)<2:
        tries-=1
        print("Wrong, you lose a life. ",tries,"tries left.")
        if tries==0:
            print("you lose")
            break
    else:
        print("Please write only one letter at the time")
        if tries==0:
            tries=-1
            print("you lose")
            break
            
# A Hangman game by atopheim
