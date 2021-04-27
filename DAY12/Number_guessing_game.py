from random import randint
from art import logo

#Attempts of game as per level of difficulty
EASY_LEVEL = 10
DIFFICULT_LEVEL = 5

def check_ans(guess, answer, turns):
    """Check answer against turn, and returns the no of turns remaining"""
    if guess > answer:
        print("Too high")
        return turns -1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it, the answer is {answer}")

#Function to set level of difficulty
def set_difficulty():
    level = input("Please choose level of difficulty as 'easy' or 'hard':")
    if level == 'easy':
        return EASY_LEVEL
    else:
        return DIFFICULT_LEVEL


#Game
def game():
    print(logo)
    #Choosing random no between 1 to 100
    print("Welcome to the number guessing game")
    print("I'm thinking of a number between 1 to 100")
    answer = randint(1, 100)
    #print(f"The correct ans is {answer}")

    turns = set_difficulty()
    guess = 0
    while guess!= answer:
        print(f"You have {turns} attempts remaining to guess the number")

        guess = int(input("Guess a number "))
        turns = check_ans(guess, answer, turns)
        if turns == 0:
            print("You are out of guesses, you lose ")
        elif guess!=answer:
            print("Guess again ")


game()
