player_1=input("Player 1 (Rock, Paper, Scissors) : ")
player_2=input("Player 2 (Rock, Paper, Scissors) : ")
action_list=["rock","paper","scissor"]

if player_1 in action_list and player_2 in action_list:
    if player_1==player_2:
        print("Draw")
    elif player_1=="rock" and player_2=="scissor": 
        print("Player 1 wins")
    elif player_1=="paper" and player_2=="rock":
        print("Player 1 wins")
    elif player_1=="scissor" and player_2=="paper":
        print("Player 1 wins")
    else: 
        print("Player 2 wins")
else:
    print("Invalid input! Please enter Rock, Paper, or Scissors.")
