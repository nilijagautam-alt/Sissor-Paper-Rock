def get_user_input(valid_choices):
    shortcuts = {
        "r": "rock",
        "p": "paper",
        "s": "scissors"
    }
    while True: 
        user_choice = input("Enter rock(r), paper(p), or scissors(s): ").lower()

        user_choice = shortcuts.get(user_choice, user_choice)


        if user_choice not in valid_choices:
            print("Oops! That's not a valid move. Please enter rock, paper, or scissors.")
        else:
            break

    return user_choice
