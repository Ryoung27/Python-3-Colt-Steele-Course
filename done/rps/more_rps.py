player_one = input("Player One Pick (R)ock, (P)aper, or (S)cisssors ")

player_two = input("Player Two Pick (R)ock, (P)aper, or (S)cisssors ")

print("Rock, Paper, Scissors, SHOOT!")

if player_one in ("R", "r") and player_two in ("S", "s"):
    print("Player One Wins")
elif player_one in ("P", "p" ) and player_two in ("R", "r"):
    print("Player One Wins")
elif player_one in ("S", "s") and player_two in ("P", "p"):
    print("Player One Wins")
elif player_two in ("P", "p" ) and player_one in ("R", "r"):
    print("Player Two Wins")
elif player_two in ("S", "s") and player_one in ("P", "p"):
    print("Player Two Wins")
elif player_two in ("R", "r") and player_one in ("S", "s"):
    print("Player Two Wins")
else:
    print("Draw")