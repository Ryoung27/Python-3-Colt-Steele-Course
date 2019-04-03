import random





def rps():
    user_input = str(input("What would you like to have (R)ock, (P)aper, or (S)cissors? "))
    computer_input = random.randint(0,2)
    if user_input not in ("R", "S", "P", "r", "s", "p") :
        print("Invalid input")
    elif user_input in ("R", "S", "P", "r", "s", "p") and computer_input == 0:
        if user_input in ("R" "r"):
            winner = "Scissors"
        elif user_input in ("S" "s"):
            winner = "Paper"
        else:
            winner = "Rock"
        print("The computer picked %s" % winner )
        print("You win!")
    elif user_input in ("R", "S", "P", "r", "s", "p") and computer_input == 1:
        if user_input in ("R" "r"):
            loser = "Paper"
        elif user_input in ("S" "s"):
            loser = "Rock"
        else:
            loser = "Scissors"
        print("The computer picked %s" % loser )
        print("You lose.")
    elif user_input in ("R", "S", "P", "r", "s", "p") and computer_input == 2:
        if user_input in ("R" "r"):
            draw = "Rock"
        elif user_input in ("S" "s"):
            draw = "Scissor"
        else:
            draw = "Paper"
        print("The computer picked %s" % draw )
        print("Draw")
    play_again = str(input("Do you want to play again? (Y/N) "))
    if play_again in ("Y", "y"):
        rps()
    else:
        print("Thanks for playing.")


rps()


