""" s => snake =>0
w => water => 1
g => gun => 2 """

import random


user_dict = {
    "s" : "snake",
    "w" : "water",
    "g" : "gun"
}

computer_dict = {
    0 : "snake",
    1 : "water",
    2 : "gun"
}

user_win = {
    "snake" : "water",
    "water" : "gun",
    "gun" : "snake"
}

def output_func(a,b):
    a = a.capitalize()
    b = b.capitalize()
    print(f"You chose '{a}'")
    print(f"Computer chose '{b}'")

while True:
    print()
    user_input = input("Enter your choice : ")
    user_input = user_input.lower()

    if(user_input in ("s","w","g")):
        computer = random.choice([0, 1, 2])
        
        user_choice = user_dict.get(user_input)
        computer_choice = computer_dict.get(computer)

        if(user_choice == computer_choice):
            output_func(user_choice,computer_choice)
            print("It's a Draw!")
        else:
            if (user_win[user_choice] == computer_choice):
                output_func(user_choice,computer_choice)
                print("You win!!")
            else:
                output_func(user_choice,computer_choice)
                print("You lose! :(")
    else:
        print("Invalid input. Exiting game.")
        break








