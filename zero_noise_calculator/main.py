import math

# Save calculation history in a file
def Save_History(Calculation):
    with open("Calculation_History.txt", "a") as history:
        history.write(f"{Calculation}\n")

# Viewcalculation History
def View_History():
    try:
        with open("Calculation_History.txt", "r") as history:
            data = history.read()
            if data.strip() == "":
                print("\nNo History Found.\n")
            else:
                print("\n––– Calculation History –––")
                print(data)
    except FileNotFoundError:
        print("\nNo History Found.\n")

# Clear all history
def Clear_History():
    with open("Calculation_History.txt", "w") as history:
        history.write("")
    print("\nHistory Cleared.\n")

# Perform calculations
def Calculation():
    print("\n––– Calculation Menu –––")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square root")
    print("6. Power")
    print("0. Exit Calculation")

    while True:

        try:
            choice = int(input("\nEnter a number (0-6): "))
        except:
            print("\nInvalid input. Please enter a number (0-6).")
            continue

        # Exit
        if choice == 0:
            print("\nExiting calculation menu. Goodbye!\n")
            break

        # Addition
        elif choice == 1:
            First_Number = float(input("\nEnter first number: "))
            Second_Number = float(input("Enter second number: "))
            Calculation = f"Calculation: {First_Number} + {Second_Number} = {First_Number + Second_Number}"

        # Subtraction
        elif choice == 2:
            First_Number = float(input("\nEnter first number: "))
            Second_Number = float(input("Enter second number: "))
            Calculation = f"Calculation: {First_Number} - {Second_Number} = {First_Number - Second_Number}"

        # Multiplication
        elif choice == 3:
            First_Number = float(input("\nEnter first number: "))
            Second_Number = float(input("Enter second number: "))
            Calculation = f"Calculation: {First_Number} × {Second_Number} = {First_Number * Second_Number}"

        # Division
        elif choice == 4:
            First_Number = float(input("\nEnter Dividend: "))
            Second_Number = float(input("Enter divisor: "))
            if  Second_Number == 0:
            	print("Error: Division by zero not allowed.")
            	continue
            else:
                Calculation = f"Calculation: {First_Number} ÷ {Second_Number} = {First_Number / Second_Number}"

        # Square root
        elif choice == 5:
            Number = float(input("\nEnter number: "))
            if Number < 0:
                print("Error: Square root of negative not allowed.")
            else:
                Calculation = f"Calculation: √{Number} = {math.sqrt(Number)}"

        # Power
        elif choice == 6:
            First_Number = float(input("\nEnter base: "))
            Second_Number = float(input("Enter exponent: "))
            Calculation = f"Calculation: {First_Number}^{Second_Number} = {math.pow(First_Number, Second_Number)}"

        else:
            print("\nInvalid choice. Please enter between 0-6.")
            continue

        # Print & Save Result
        print(Calculation)
        Save_History(Calculation)


# Main Calculator Menu
while True:
    print("=== Zero-Noise Calculator ===")
    print("1. Perform Calculation")
    print("2. View History")
    print("3. Clear History")
    print("0. Exit Program")

    try:
        menu_choice = int(input("\nEnter your choice: "))
    except:
        print("\nInvalid input. Please enter a number (0-3).\n")
        continue

    if menu_choice == 1:
        Calculation()
    elif menu_choice == 2:
        View_History()
    elif menu_choice == 3:
        Clear_History()
    elif menu_choice == 0:
        print("\nThanks for using the calculator. Stay smart, Saylenc!\n")
        break
    else:
        print("\nInvalid choice. Please enter between 0-3.")
