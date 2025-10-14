import datetime
import random
import json

# -----------------------------------------------------------------
# MOTIVATIONAL LINES (SYSTEM MESSAGES)
# -----------------------------------------------------------------

# Message when a new habit is added
ADD_HABIT_QUOTES = [
    "Habit added. Discipline activated.",
    "Another step toward mastery.",
    "Quiet move. Loud results.",
    "New system logged. Keep it consistent.",
    "You just coded your future behavior.",
    "Habit installed. Now execute daily.",
    "Action recorded. Momentum begins.",
    "Added. Now make it unbreakable.",
    "Routine added. Greatness under construction.",
    "Silent setup. Massive impact loading..."
]

# Message when user exits the system
EXIT_QUOTES = [
    "Session closed. Progress saved.",
    "Discipline logged out, not stopped.",
    "Quiet exit. Growth continues.",
    "Ledger locked. Keep your streak alive.",
    "You moved one step further today.",
    "System shut down. Mind stays active.",
    "Exit confirmed. Stay consistent, Saylenc.",
    "Silent end. The mission never stops.",
    "Habit Ledger sealed. Tomorrow awaits.",
    "Closing the log. Keep building quietly."
]

# -------------------------
# ADD NEW HABIT
# -------------------------
def add_habit():
    """Add a new habit into the JSON file."""
    user_habit = input("\nEnter a new habit to add: ").strip()
    print(f"\n{random.choice(ADD_HABIT_QUOTES)}\n")

    try:
        with open("Habits_History.json", "r") as file:
            habits = json.load(file)
            if not isinstance(habits, list):
                habits = []
    except (FileNotFoundError, json.JSONDecodeError):
        habits = []

    new_habit = {
        "Habit": user_habit,
        "Streak": 0,
        "Last Done": None
    }

    habits.append(new_habit)
    with open("Habits_History.json", "w") as file:
        json.dump(habits, file, indent=4)


# ----------------------------------
# MARK HABIT AS DONE
# ----------------------------------
def mark_habit_done():
    """Mark a selected habit as completed today and update its streak."""
    try:
        with open("Habits_History.json", "r") as file:
            habits = json.load(file)
    except FileNotFoundError:
        print("\nNo habits file found. Try adding habits first.\n")
        return
    except json.JSONDecodeError:
        print("\nJSON file is corrupted or unreadable.\n")
        return

    if not habits:
        print("\nNo habits found. Add some first.\n")
        return

    print("\n––– Choose a Habit to Mark as Done –––\n")
    for index, habit in enumerate(habits, start=1):
        print(f"{index}. {habit['Habit']} (Streak: {habit['Streak']})")

    try:
        choice = int(input(f"\nEnter number (1-{len(habits)}): "))
    except ValueError:
        print("\nInvalid input. Please enter a valid number.\n")
        return

    if choice < 1 or choice > len(habits):
        print("\nNumber out of range.\n")
        return

    # Selected habit
    habit = habits[choice - 1]
    today = datetime.date.today().isoformat()

    # Check if already done today
    if habit["Last Done"] == today:
        print(f"\n'{habit['Habit']}' is already marked done today.\n")
    else:
        # If done yesterday, continue streak. Else, reset.
        last_done = habit["Last Done"]
        if last_done:
            last_date = datetime.date.fromisoformat(last_done)
            if (datetime.date.today() - last_date).days == 1:
                habit["Streak"] += 1
            else:
                habit["Streak"] = 1
        else:
            habit["Streak"] = 1

        habit["Last Done"] = today
        print(f"\nHabit '{habit['Habit']}' marked done for today. Streak: {habit['Streak']}\n")

    with open("Habits_History.json", "w") as file:
        json.dump(habits, file, indent=4)


# ----------------------------
# EDIT HABIT NAME
# ----------------------------
def edit_habit():
    """Edit the name of an existing habit."""
    try:
        with open("Habits_History.json", "r") as file:
            habits = json.load(file)
    except FileNotFoundError:
        print("\nNo habits file found.\n")
        return

    if not habits:
        print("\nNo habits to edit.\n")
        return

    print("\n––– Edit Habit Name –––\n")
    for index, habit in enumerate(habits, start=1):
        print(f"{index}. {habit['Habit']}")

    try:
        choice = int(input(f"\nEnter the habit number to edit (1-{len(habits)}): "))
    except ValueError:
        print("\nInvalid input. Please enter a number.\n")
        return

    if choice < 1 or choice > len(habits):
        print("\nInvalid choice.\n")
        return

    new_name = input("Enter the new name for the habit: ").strip()
    if not new_name:
        print("\nHabit name cannot be empty.\n")
        return

    old_name = habits[choice - 1]["Habit"]
    habits[choice - 1]["Habit"] = new_name

    with open("Habits_History.json", "w") as file:
        json.dump(habits, file, indent=4)

    print(f"\nHabit '{old_name}' successfully renamed to '{new_name}'.\n")


# ---------------------------
# VIEW ALL HABITS
# ---------------------------
def view_habits():
    """Display all habits with their streaks and last completion date."""
    try:
        with open("Habits_History.json", "r") as file:
            habits = json.load(file)
    except FileNotFoundError:
        print("\nNo habits file found.\n")
        return
    except json.JSONDecodeError:
        print("\nJSON file is unreadable.\n")
        return

    if not habits:
        print("\nNo habits found.\n")
        return

    print("\n––– Habit Overview –––\n")
    for index, habit in enumerate(habits, start=1):
        print(f"{index}. {habit['Habit']}")
        print(f"   Streak: {habit['Streak']}")
        print(f"   Last Done: {habit['Last Done']}\n")


# -----------------------------
# CLEAR ALL HABITS
# -----------------------------
def clear_habits():
    """Erase all habits from the JSON file."""
    with open("Habits_History.json", "w") as file:
        json.dump([], file)
    print("\nAll habits cleared from the ledger.\n")


# ----------------------------------
# MAIN PROGRAM LOOP
# ----------------------------------
while True:
    print("=== Habit Ledger ===")
    print("1. Add a new habit")
    print("2. Mark habit as done")
    print("3. Edit a habit name")
    print("4. View all habits")
    print("5. Clear all habits")
    print("0. Exit")

    try:
        option = int(input("\nEnter your choice (0–5): "))
    except ValueError:
        print("\nInvalid input. Enter a number (0–5).\n")
        continue

    if option == 0:
        print(f"\n{random.choice(EXIT_QUOTES)}\n")
        break
    elif option == 1:
        add_habit()
    elif option == 2:
        mark_habit_done()
    elif option == 3:
        edit_habit()
    elif option == 4:
        view_habits()
    elif option == 5:
        clear_habits()
    else:
        print("\nInvalid choice. Try again.\n")
