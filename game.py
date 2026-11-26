import random

choice_list = ["stone", "paper", "scissor"]
comp_score = 0
player_score = 0
options = {1:"stone", 2:"paper", 3:"scissor"}
print(options)

for i in range(3):
    player_choice = int(input("Enter the choice: "))
    if player_choice >= 4:
        print("The option number cannot exceed the number 3")
        continue
    print("You have choose the optiion : ", options[player_choice])
    comp_choice = random.choice(choice_list)
    print("computer choice is :", comp_choice)
    if player_choice == 1 and comp_choice == "paper" : 
        comp_score += 1
    elif player_choice == 1 and comp_choice == "stone":
        None
    elif player_choice == 1 and comp_choice == "scissor":
        player_score +=1
    elif player_choice == 2 and comp_choice == "scissor":
        comp_score +=1
    elif player_choice == 2 and comp_choice == "stone":
        player_score += 1
    elif player_choice == 2 and comp_choice == "paper":
        None
    elif player_choice == 3 and comp_choice == "paper":
        player_score += 1
    elif player_choice == 3 and comp_choice == "stone":
        comp_score += 1
    elif player_choice == 3 and comp_choice == "scissor":
        None
    

if comp_score > player_score :
    print('Computer won')
elif comp_score < player_score :
    print("You Won")
elif comp_score == player_score:
    print("Match is draw")
print("Total match score : ")
print("Your Score: ",player_score)
print("Computer score: ",comp_score)

