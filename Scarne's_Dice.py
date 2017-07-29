import random

# Mark Erickson
# CS 375 Programming Project
# This program lets the user play a dice game. First to 100 wins. 1's end your turn.
# Hold to keep your score or keep rolling

# winCheck checks if someone has 100 points or more
def winCheck(userScore,computerScore):
    if userScore >= 100:
        print('You win!')
        exit
    elif computerScore >= 100:
        print('You lose!')
        exit

# rollDie generates a random number between 1 and 6
def rollDie():
    roll = random.randint(1,6)
    if roll == 1:
        return 1
    else:
        return roll

userScore = 0 # total player score
userTurnScore = 0 # player's turn score
computerTurnScore = 0 # computer's turn score
computerScore = 0 # computer's total score
roll = 0
while (userScore < 100 and computerScore < 100):
    while (roll != 1): # loop until user rolls a 1
        choice = input("Roll(r) Hold(h) Exit(e)?")
        if choice == 'r': # User wants to roll again
            roll = rollDie()
            print("You rolled a " + str(roll))
            if roll == 1: # user rolled a 1 so end the turn
                break
            userTurnScore += roll
            print("Your turn score:" + str(userTurnScore))
        elif choice == 'h': # user holds so add his turn score
            userScore += userTurnScore
            break
        elif choice == 'e': # exit program
            exit
        else:
            print("Command not recognized.")
    userTurnScore = 0
    roll = 0
    
    winCheck(userScore,computerScore)
    while (computerTurnScore <= 15): # the computer will keep rolling until it has 15 for its turn score and then holds
        compRoll = rollDie()
        print("The computer rolled a " + str(compRoll))
        if compRoll == 1: # computer rolled a 1 so its turn ends
            computerTurnScore = 0
            break
        else:
            computerTurnScore += compRoll
            
    computerScore += computerTurnScore
    computerTurnScore = 0
    print ("User Score:" + str(userScore) + " Computer Score:" + str(computerScore))
    winCheck(userScore,computerScore)
    
    
            