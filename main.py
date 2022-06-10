import random

while True:
    user = input("Enter choice \n R for Rock \n P for Paper \n S for Scissors: ")

    options = ["R", "P", "S"]
    computer_choice = random.choice(options)
    if user in options:
        print("Player", [user], ": CPU", [computer_choice])

        if user == computer_choice:
            print("It's a tie! Both players Picked", (user))
        elif user == "R":
            if computer_choice == "P":
                print("Paper covers Rock. \nYou lose")
            else:
                print("Rock breaks Scissors. \nYou win!")
        elif user == "P":
            if computer_choice == "R":
                print("Paper covers Rock.\nYou win!")
            else:
                print("Scissors cuts Paper. \nYou lose")
        elif user == "S":
            if computer_choice == "P":
                print("Scissors cuts paper. \nYou win!")
            else:
                print("Rock breaks scissors. \nYou lose")

        again = input("Another round? (Y/N): ")
        if again == "N":
            print("Goodbye!")
            break



    else:
        print("Invalid Input")
