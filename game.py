"""Creating Random No. guess Python Game"""
import os
import math as mt
from random import randrange
print("="*50)
print("\tGuess The Number Python Game!")
print("="*50)

print("""Select Difficulty Level :-
1. Easy Mode(8 Guess)
2. Difficult Mode(5 Guess)""")
wonGame=False
# Defining Engine Function that will handle the game!
def EngineGame(noGuess):
    global wonGame
    guessNo = randrange(1, 30)
    print(f"Random Guess No.(1-30) generated! You have a total of {noGuess} Guesses!")
    while noGuess!=0:
        noEntered = int(input("Enter your Guess :- "))
        if mt.fabs(noEntered-guessNo) == 0:
            guessLeft = noGuess-1
            noGuess=0
            wonGame=True
        elif mt.fabs(noEntered-guessNo) <= 5:
            print("\nAnswer is not right but you are near to the Answer. :)")
            noGuess -= 1
            print(f"You have only {noGuess} Guesses Left!\n")
        elif mt.fabs(noEntered-guessNo) <= 10:
            print("\nHmmm, This is not looking right! :(")
            noGuess -= 1
            print(f"You have only {noGuess} Guesses Left!\n")
        elif mt.fabs(noEntered-guessNo) > 10:
            print("\nNo, your guess is not right! :(")
            noGuess -= 1
            print(f"You have only {noGuess} Guesses Left!\n")
        else :
            pass
    else :
        if wonGame==True:
            print("\nCongratulations! You have successfully guessed the right No. :)")
            print(f"You have found the right Answer with {guessLeft} Guesses Left!\n")
        else :
            print("\nSorry! You have lost the Game! ")
            print(f"Right Answer is {guessNo}.\n")
# Interacting with user in first Screen.
ch = int(input("Select Difficulty Level (1 or 2) => "))
if ch==1:
    print("You Have Chosen Easy Mode!")
    EngineGame(8)
elif ch==2 :
    print("Well Done! You are a Brave Human ! You have Chosen Difficult Mode!")
    EngineGame(5)
else :
    print("Please Choose a valid Option(1 or 2) !")
os.system('pause')