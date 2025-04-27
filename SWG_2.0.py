print("//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
print("//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
print("//////////////////////////////////////////   THE GAME OF SNAKE WATER GUN   ///////////////////////////////////////////")
print("//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
print("//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")


import random
computer = random.choice([0,1,-1])

valid_inputs = ["s", "w", "g"]
dict_def ={"s":0, "w":1, "g":-1}
reverse_dict = {0:"Snake", 1:"Water", -1:"Gun"}

def choice():
    print("How to choose : ", end = "")
    print("  Snake    Water   Gun\n                    s        w      g \n")

    user_in = input("Enter your choice : ").lower()
    if(user_in in valid_inputs):
        return user_in
    else:
        print("\n\n")
        print("Please enter a valid input")
        return choice()
    
user_in = choice()
user_choice = dict_def[user_in]

print(f"You chose {reverse_dict[user_choice]}\nThe computer chose {reverse_dict[computer]}")
print("The result is given below : ")
if(computer == user_choice):
    print("It's a DRAW!")
else:
    if(computer==0 and user_choice==1):
        print("YOU LOSE!")
    elif(computer==0 and user_choice==-1):
        print("YOU WIN!")
    elif(computer==1 and user_choice==-1):
        print("YOU LOSE!")
    elif(computer==1 and user_choice==0):
        print("YOU WIN!")
    elif(computer==-1 and user_choice==1):
        print("YOU WIN!")
    elif(computer==-1 and user_choice==0):
        print("YOU LOSE!")
    else:
        print("There is some error!")
