import os
import random

def roll():
    return random.randint(1, 6)

def save_results(filename, players, scores, winner_idx):
    with open(filename, "w") as file:
        file.write(f"Number of players: {players}\n")
        file.write(f"Final Scores: {scores}\n")
        file.write(f"Winner: Player {winner_idx + 1} with {scores[winner_idx]} points!\n")

# Always save file next to pig.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(BASE_DIR, "PIG_Results.txt")

print("Welcome to the Pig Game!")
print("\nRules:")
print("1. Each player takes turns rolling a die.")
print("2. If you roll a 1, your turn ends, and you lose all points for that turn.")
print("3. If you roll 2-6, the value is added to your turn score.")
print("4. You can choose to roll again or hold.")
print("5. If you hold, your turn score is added to your total score.")
print("6. The first player to reach 50 points wins.\n")

max_score = 50

while True:
    players_input = input("Enter the number of players (2-4): ")
    if players_input.isdigit():
        players = int(players_input)
        if 2 <= players <= 4:
            break
    print("Invalid input. Enter a number between 2 and 4.")

player_scores = [0] * players
winner = None

while winner is None:
    for player_idx in range(players):
        print(f"\n--- Player {player_idx + 1}'s Turn ---")
        current_score = 0

        while True:
            should_roll = input("\nRolling (y/n)? ").strip().lower()
            if should_roll != "y":
                break

            value = roll()
            if value == 1:
                print("Whoops, rolled a 1! Turn over. No points earned.")
                current_score = 0
                break
            else:
                current_score += value
                print(f"Rolled: {value}. Current Score: {current_score}")
                print(f"Total potential score: {player_scores[player_idx] + current_score}")

            # Check immediately if adding this roll will hit max_score
            if player_scores[player_idx] + current_score >= max_score:
                player_scores[player_idx] += current_score
                winner = player_idx
                break  # Stop rolling AND end the game

        if winner is not None:
            break  # Stop the for-loop too

        player_scores[player_idx] += current_score
        print(f"Your total score is now: {player_scores[player_idx]}")

# Save results
save_results(FILENAME, players, player_scores, winner)

print(f"\nCongrats Player {winner + 1}!!! You win with {player_scores[winner]} points!")
print(f"Results saved to: {FILENAME}")
