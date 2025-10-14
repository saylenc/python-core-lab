import random
import json


# ----------------------------
# Save Game History
# ----------------------------
def save_game_history(new_result):
    """Appends the new game result to JSON file safely."""
    try:
       # Try loading existing data
        with open("Guess_Data.json", "r") as history_file:
            data = json.load(history_file)
            if not isinstance(data, list):
                data = []
    except (FileNotFoundError, json.JSONDecodeError):
        data = []  # Start new list if file doesn't exist or is broken

    # Add new result
    data.append(new_result)

    # Write full list back to file
    with open("Guess_Data.json", "w") as history_file:
        json.dump(data, history_file, indent=4)
       

# -----------------------------
# View Game History
# -----------------------------
def view_game_history():
    """Displays stored guessing results in structured form."""
    try:
        with open("Guess_Data.json", "r") as history_file:
            data = json.load(history_file)

            if not data:
                print("\nNo game history found.\n")
                return

            print("\n=== Game History ===")
            for index, record in enumerate(data, start=1):
                print(f"  Correct Guess: {record['Correct Guess']}")
                print(f"  Attempts: {record['Attempts']}")
    except FileNotFoundError:
        print("\nNo game history file found.\n")
    except json.JSONDecodeError:
        print("\nHistory file is corrupted or not in readable JSON format.\n")

# -----------------------------
# Clear Game History
# -----------------------------
def clear_game_history():
    """Clears all saved game history safely."""
    try:
        with open("Guess_Data.json", "w") as history_file:
            json.dump([], history_file)  # Write valid empty JSON list
        print("\nHistory cleared successfully.\n")
    except Exception as e:
        print(f"\nError clearing history: {e}\n")

# ---------------------------------
# Single Guessing Game
# ---------------------------------
def start_guessing_game():
    """Runs one round of the number guessing game."""
    while True:
        print("\n=== Number Guess Game ===")
        print("1. Use default range (1–100)")
        print("2. Use custom range\n")

        try:
            choice = int(input("Enter your choice (1 or 2): "))
        except ValueError:
            print("\nInvalid input. Please enter 1 or 2.")
            continue

        # --- Default range (1–100)
        if choice == 1:
            secret_number = random.randint(1, 100)
            attempts = 1

            while True:
                try:
                    guess = int(input("\nEnter your guess (1–100): "))
                except ValueError:
                    print("\nInvalid input. Please enter a number.")
                    continue

                if guess < 1 or guess > 100:
                    print("\nOut of range! Choose between 1 and 100.")
                elif guess > secret_number:
                    print("\nToo high! Try again.")
                elif guess < secret_number:
                    print("\nToo low! Try again.")
                else:
                    result = {
                        "Correct Guess": secret_number,
                        "Attempts": attempts
                    }
                    save_game_history(result)
                    print(f"\nCorrect! You guessed {secret_number} in {attempts} attempts.")
                    break
                attempts += 1

        # --- Custom range
        elif choice == 2:
            try:
                start_range = int(input("\nEnter starting number: "))
                end_range = int(input("Enter ending number: "))
            except ValueError:
                print("\nInvalid input. Please enter valid numbers.")
                continue

            secret_number = random.randint(start_range, end_range)
            attempts = 1

            while True:
                try:
                    guess = int(input(f"\nEnter your guess ({start_range}–{end_range}): "))
                except ValueError:
                    print("\nInvalid input. Please enter a number.")
                    continue

                if guess < start_range or guess > end_range:
                    print(f"\nOut of range! Choose between {start_range} and {end_range}.")
                elif guess > secret_number:
                    print("\nToo high! Try again.")
                elif guess < secret_number:
                    print("\nToo low! Try again.")
                else:
                    result = {
                        "Correct Guess": secret_number,
                        "Attempts": attempts
                    }
                    save_game_history(result)
                    print(f"\nYou nailed it! {secret_number} guessed in {attempts} attempts.")
                    break
                attempts += 1

        else:
            print("\nPlease choose only 1 or 2.")
            continue
        break


# ------------------------------
# Game Loop (Replay)
# ------------------------------
def game_loop():
    """Allows the user to play multiple rounds."""
    start_guessing_game()
    while True:
        replay = input("\nPlay again? (y/n): ").lower()
        if replay == "y":
            start_guessing_game()
        elif replay == "n":
            print("\nThank you for playing. Goodbye!\n")
            break
        else:
            print("\nInvalid input. Please enter 'y' or 'n'.")


# -----------------
# Main Menu
# -----------------
while True:
    print("=== Guess Game Menu ===")
    print("1. Play Game")
    print("2. View History")
    print("3. Clear History")

    try:
        menu_choice = int(input("\nEnter your choice (1-3): "))
    except ValueError:
        print("\nInvalid input. Please enter a number (1, 2 or 3).")
        continue

    if menu_choice == 1:
        game_loop()
    elif menu_choice == 2:
        view_game_history()
    elif menu_choice == 3:
    	clear_game_history()
    else:
        print("\nInvalid choice. Please select 1, 2 or 3.")
