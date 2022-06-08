import random
options = ["R", "P", "S"]
game_on = True
while game_on:
    print("Welcome to the Rock-Paper-Scissors game")
    user_choice = input("Choose any of R, P or S : \n")
    user_choice = user_choice.upper()
    computer_choice = random.choice(options)
    print("Player : " + user_choice)
    print("CPU :" + computer_choice)
    if user_choice == computer_choice:
        print("Its a tie")
        pass
    elif user_choice == "P" and computer_choice == "R":
        print("You won! Do you want to play again?")
        choice = input("1 for Yes. 2 for No :  \n")
        if choice == "1":
            pass
        else:
            game_on = False
            print("Thank you for playing")
    elif user_choice == "R" and computer_choice == "S":
        print("You won! Do you want to play again?")
        choice = input("1 for Yes. 2 for No :  \n")
        if choice == "1":
            pass
        else:
            game_on = False
            print("Thank you for playing")
    elif user_choice == "S" and computer_choice == "P":
        print("You won! Do you want to play again?")
        choice = input("1 for Yes. 2 for No :  \n")
        if choice == "1":
            pass
        else:
            game_on = False
            print("Thank you for playing")
    elif user_choice == "S" and computer_choice == "R":
        print("You lost. Start afresh")
        pass
    elif user_choice == "R" and computer_choice == "P":
        print("You lost. Start afresh")
        pass
    elif user_choice == "P" and computer_choice == "S":
        print("You lost. Start afresh")
        pass
    else:
        print("Invalid selection. Try again")
        pass

