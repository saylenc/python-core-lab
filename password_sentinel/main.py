import string 

# Step 1: Check if password is empty or made of repeated characters
def basic_checks(password):
    if password == "":
        print("\nPassword is empty!")
        print("Suggestion: Try writing some characters.")
    elif len(set(password)) == 1 and len(password) > 1:
        print("\nWeak password! Made of repeated characters.")
        print("Suggestion: Use different characters, not just one repeated.")
    else:
    	check_common_passwords(password)


# Step 2: Check against common passwords list
def check_common_passwords(password):
    with open("Common_Passwords.txt") as file:
        common_passwords = file.read().splitlines()
        
    if password in common_passwords:
        print("\nWeak password! This is a common password.")
        print("Suggestion: Make something unique, avoid common patterns.")
    else:
        analyze_strength(password)


# Step 3: Analyze password strength by rules
def analyze_strength(password):
    has_letters = any(ch.isalpha() for ch in password)
    has_numbers = any(ch.isdigit() for ch in password)
    has_symbols = any(ch in string.punctuation for ch in password)

    # Weak Password
    if len(password) < 8:
        print("\nWeak password! Less than 8 characters.")
        print("Suggestion: Use at least 8 characters.")
    elif (has_letters + has_numbers + has_symbols) < 2:
        print("\nWeak password! Only one type of character used.")
        print("Suggestion: Mix letters, numbers, and symbols.")

    # Medium Password
    elif 8 <= len(password) <= 12 and (has_letters + has_numbers + has_symbols) >= 2:
        print("\nMedium password.")
        print("Suggestion: Add more length to make it stronger.")
    elif len(password) >= 13 and (has_letters + has_numbers + has_symbols) == 2:
        print("\nMedium password.")
        print("Suggestion: Add the missing character type for strength.")

    # Strong Password
    elif len(password) >= 13 and (has_letters + has_numbers + has_symbols) == 3:
        print("\nStrong password! Secure and well-balanced.")


# Core Menu / Brain of the program
def sentinel_menu():
    while True:
        print("––– Password Sentinel –––")
        print("1. Check password strength")
        print("2. Generate strong password (coming soon)")
        
        try:
            user_choice = int(input("\nEnter your choice (1-2): "))
        except ValueError:
            print("\nInvalid input. Please enter a number (1 or 2).\n")
            continue
        
        if user_choice == 1:
            password = input("\nEnter a password: ").replace(" ", "").lower()
            basic_checks(password) 
        elif user_choice == 2:
            print("\nPassword generator feature coming soon...")
        else:
            print("\nInvalid choice. Please enter 1 or 2.\n")
            continue
        break


# Initial call
sentinel_menu()

# Loop until user wants to quit
while True:
    user_choice = input("\nDo you want to use Password Sentinel again? (y/n): ").lower()
    
    if user_choice == "y":
        print()  # Just for cleaner spacing
        sentinel_menu()
    elif user_choice == "n":
        print("\nThanks for using Password Sentinel. Stay safe!")
        break
    else:
        print("\nInvalid input. Please enter 'y' or 'n' only.")
