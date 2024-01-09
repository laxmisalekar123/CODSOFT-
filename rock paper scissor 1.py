from random import randint
randomvariable = ["rock","paper","scissor"]
computer=randomvariable[randint(0,2)]
player=True
while player == True:
    player = input("rock , paper ,scissor")
    if player == computer:
        print("Its a tie!!!")
    elif player =="scissor":
        if computer =="rock":
            print("You loose")
        else:
            print("You win")
    elif player == "rock":
         if computer == "paper":
            print("You loose")
         else:
            print("You win")
    else:
        pass



