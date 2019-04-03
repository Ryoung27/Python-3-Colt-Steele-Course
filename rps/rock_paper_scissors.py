import random

user_input = str(input("What would you like to have (R)ock, (P)aper, or (S)cissors? "))

computer_input = random.randint(0,2)

# if "a" != "b":
#     print("Worked")
# else:
#     print("NO")

if user_input not in ("R", "S", "P", "r", "s", "p") :
    print("Invalid input")
elif user_input in ("R", "S", "P", "r", "s", "p") and computer_input == 0:
    print("You win!")
elif user_input in ("R", "S", "P", "r", "s", "p") and computer_input == 1:
    print("You lose.")
elif user_input in ("R", "S", "P", "r", "s", "p") and computer_input == 2:
    print("Draw")