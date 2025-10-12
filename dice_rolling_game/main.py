import random

# Save dice roll history to a file
def save_history(entry):
    with open("Dice_History.txt", "a") as file:
        file.write(entry)

# View dice roll history from file
def view_history():
    try:
        with open("Dice_History.txt", "r") as file:
            data = file.read()
            if data.strip() == "":
                print("\nNo history found.\n")
            else:
                print("\n––– Dice Roll History –––")
                print(data)
    except FileNotFoundError:
        print("\nNo history file found.\n")

# Clear dice roll history file
def clear_history():
    with open("Dice_History.txt", "w") as file:
        file.write("")

# Main dice rolling function
def roll_dice():
    while True:
        # Computer rolls dice
        computer_dice1 = random.randint(1, 6)
        computer_dice2 = random.randint(1, 6)

        user_choice = input("\nRoll the dice? (y/n): ").lower().strip()

        if user_choice == "":
            print("\nInvalid input. You entered nothing.")
        elif user_choice == "y":
            user_dice1 = random.randint(1, 6)
            user_dice2 = random.randint(1, 6)
            print(f"\nYou rolled {user_dice1}, {user_dice2} and Computer rolled {computer_dice1}, {computer_dice2}.")
            entry = f"Your dice: {user_dice1}, {user_dice2} | Computer dice: {computer_dice1}, {computer_dice2}\n"
            save_history(entry)
        elif user_choice == "n":
            print("\nExiting dice roll. See you again.\n")
            break
        else:
            print("\nInvalid input. Please enter only 'y' or 'n'.")

# Main menu loop
while True:
    print("––– Dice Game Menu –––")
    print("1. Roll Dice")
    print("2. View History")
    print("3. Clear History")

    try:
        choice = int(input("\nEnter your choice (1-3): "))
    except ValueError:
        print("\nInvalid input. Please enter a number (1-3).\n")
        continue

    if choice == 1:
        roll_dice()
    elif choice == 2:
        view_history()
    elif choice == 3:
        clear_history()
        print("\nHistory cleared!\n")
    else:
        print("\nInvalid choice. Please enter between 1 and 3.\n")
