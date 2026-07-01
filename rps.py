import random
import os


# Constants
HEATS = 3
FILENAME = "RPS_Results.txt"


def intro():
    print("Welcome to Rock-Paper-Scissors!")
    print("Challenge your logic and see if you can beat the computer.\n")


def user_authentication():
    print("Do you want to create an account? (y/n)")
    while True:
        choice = input().lower().strip()
        if choice == "y":
            while True:
                username = input("Enter your username (min 3 characters): ").strip()
                if len(username) >= 3:
                    break
                print("Username must be at least 3 characters. Try again.")
            while True:
                password = input("Enter your password (min 6 characters): ").strip()
                if len(password) >= 6:
                    print(f"Your account is created. Welcome, {username}!")
                    return username
                print("Password must be at least 6 characters. Try again.")
        elif choice == "n":
            username = "Guest"
            print("You are logged in as a Guest.")
            return username
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def game_instructions(username):
    print(f"\nWelcome, {username}!")
    print("\nGameplay Instructions:")
    print(f"You will play {HEATS} heats of Rock-Paper-Scissors.")
    print("The rules are simple:")
    print("- Rock beats Scissors\n- Scissors beats Paper\n- Paper beats Rock\n")
    print("Make your choice each heat and try to outscore the computer!\n")


def play_heat():
    options = ["rock", "paper", "scissors"]


    while True:
        user_choice = input("Rock, paper, or scissors? ").lower().strip()
        if user_choice in options:
            break
        print("Invalid choice. Must be rock, paper, or scissors.")


    computer_choice = random.choice(options)
    print(f"You chose {user_choice}.")
    print(f"The computer chose {computer_choice}.")


    if user_choice == computer_choice:
        print("It's a tie!")
        return 0  # Tie
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print(f"{user_choice.capitalize()} beats {computer_choice}. You win this heat!")
        return 1  # Player wins
    else:
        print(f"{computer_choice.capitalize()} beats {user_choice}. The computer wins this heat!")
        return -1  # Computer wins


def save_results(username, games_played, games_won, scores):
    with open(FILENAME, "w") as file:
        file.write(f"Username: {username}\n")
        file.write(f"Games Played: {games_played}\n")
        file.write(f"Games Won: {games_won}\n")
        file.write("Score(s):\n")
        for i, score in enumerate(scores, 1):
            file.write(f"Round {i}: {score}\n")


def play_again(username):
    while True:
        choice = input(f"{username}, do you want to play another game? (y/n): ").lower().strip()
        if choice == "y":
            print("Starting a new game...")
            return True  # Indicates the game should restart
        elif choice == "n":
            print("Thanks for playing! Goodbye!")
            return False  # Indicates the game should end
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def main():
    intro()
    username = user_authentication()


    games_played = 0
    games_won = 0
    all_scores = []


    while True:
        print(f"\nHello, {username}! Get ready to play Rock-Paper-Scissors!")
        player_score = 0
        computer_score = 0


        for heat_num in range(1, HEATS + 1):
            print(f"\n--- Heat {heat_num} ---")
            result = play_heat()
            if result == 1:
                player_score += 1
            elif result == -1:
                computer_score += 1
            print(f"SCOREBOARD: Player {player_score} | Computer {computer_score}")


        print("\n--- Final Results ---")
        if player_score > computer_score:
            print(f"Congratulations, {username}! You won this game with a score of {player_score}.")
            games_won += 1
        elif player_score < computer_score:
            print(f"The computer wins this game with a score of {computer_score}.")
        else:
            print("It's a tie!")


        games_played += 1
        all_scores.append(f"Player {player_score} | Computer {computer_score}")


        save_results(username, games_played, games_won, all_scores)


        if not play_again(username):
            break


if __name__ == "__main__":
    main()