# # The ouputs
# x = ["Stone", "Paper", "Scissor"]
# y = "Paper"
# z = "Scissor"

# # The main code
# b = input()
# if b == "Stone" or b == "stone" or b == "Paper" or b == "paper" or b == "Scissor" or b ==  "scissor":
#     print(x))

from random import randint
 
t = ["Stone", "Paper", "Scissors"]
output = t[randint(0,2)]


i = False
while i == False:
    i = input("Paper, Scissors, Stone?")
    print(output)
    if i == output:
        print("tie")

    elif i == "Paper" or i == "paper":
        if output == "Stone":
            print("You win!!! Paper covers stone")
        else:
            print("You lose")
                       

    elif i == "Scissors" or i == "scissors":
        if output == "Paper":
            print("You win!!! Scissors cuts paper")
        else:
            print("You lose")
                        

    elif i == "Stone" or i == "stone":
        if output == "Scissors":
            print("You win!!! Stone smashes scissor")
        else:
            print("You lose")
            
    else:
        print("Please choose the option correctly")
                  
    i = False
# mainGame()
# mainGame()

    