from random import randint

play_again = None
def guessing_game():
    user_guess = int(input("Guess a number between 1 and 10: "))
    number = randint(1,10)
    while user_guess != number:
        print("Please guess again.")
        user_guess = int(input("Guess a number between 1 and 10: "))
    if user_guess == number:
        print("Congratulations, did you just read my mind?")


    play_again = input("Do you want to play again? (y/n) ")
    if play_again in ("Y", 'y'):
        guessing_game()
    else:
        print("Thanks for playing")


guessing_game()



