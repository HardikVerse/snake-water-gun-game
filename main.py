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

user_win = {                         #Only cases where user can win..
    "snake" : "water",
    "water" : "gun",
    "gun" : "snake"
}

def output_func(a,b):
    a = a.capitalize()
    b = b.capitalize()
    print(f"You chose '{a}'")
    print(f"Computer chose '{b}'")

def point_count(user,computer):
    print(f"\nYour point is {user}")
    print(f"Computer point is {computer}\n")

point_user = 0 
point_computer = 0

def round_win(points,winner):
    if(points == 5):
        
        print(f"{winner} Won🏆!!")
        print("Enter your choice below to start new round")
        print()
        point_user = 0 
        point_computer = 0


    
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
            point_count(point_user,point_computer)
        else:
            if (user_win[user_choice] == computer_choice):
                output_func(user_choice,computer_choice)
                print("You won!!")
                point_user += 1
                point_count(point_user,point_computer)

                if(point_user == 5):
                    print(f"You are winner🏆!!")
                    print("Enter your choice below to start new round")
                    print()
                    point_user = 0 
                    point_computer = 0
                
            else:
                output_func(user_choice,computer_choice)
                print("You lose! :(")
                point_computer += 1
                point_count(point_user,point_computer)
                if(point_computer == 5):
                    print(f"Computer is winner🏆!!")
                    print("Enter your choice below to start new round")
                    print()
                    point_user = 0 
                    point_computer = 0
    else:
        print("Invalid input. Exiting game.")
        break









