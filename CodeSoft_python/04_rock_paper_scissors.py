import random

def determine_winner(user_choice, computer_choice):
    # Define the winning conditions
    winning_conditions = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }

    # Check if it's a tie
    if user_choice == computer_choice:
        return "It's a tie!"
    # Check if user wins
    elif winning_conditions[user_choice] == computer_choice:
        return "You win!"
    # Otherwise, computer wins
    else:
        return "Computer wins!"

def main():
    user_score = 0
    computer_score = 0

    while True:
        print("\nRock, Paper, Scissors Game")
        print("Choose one: (rock, paper, scissors)")
        user_choice = input("Your choice: ").lower()

        # Validate user input
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please choose from 'rock', 'paper', or 'scissors'.")
            continue

        # Generate computer's choice
        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        print(f"Your choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")

        # Determine the winner and display the result
        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Update scores
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"Score - You: {user_score}, Computer: {computer_score}")

        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
