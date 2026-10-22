def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Draw!"

    elif user_choice == "rock" and computer_choice == "scissors":
        return "You win!"

    elif user_choice == "scissors" and computer_choice == "paper":
        return "You win!"

    elif user_choice == "paper" and computer_choice == "rock":
        return "You win!"

    else:
        return "You lose!"
