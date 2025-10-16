import string
import time
import json

# ------------------------
# GET TEXT FILE
# ------------------------
def take_file():
    """Ask user for a text file and verify it's a .txt file before processing."""
    file_name = input("\nEnter the name of a text file (e.g. article.txt): ").strip()
    
    if not file_name.endswith(".txt"):
        print("\nInvalid format. File must be a .txt file.\n")
    else:
        read_file(file_name)

# -----------------
# READ FILE
# -----------------
def read_file(file_name):
    """Read all contents from a .txt file (book, article, etc.)."""
    try:
        with open(file_name, "r") as text_file:
            text = text_file.read()
    except FileNotFoundError:
        print("\nText file not found.\n")
        return
    
    if text.strip() == "":
        print("\nText file is empty.\n")
    else:
        print("\nProcessing...\n")
        time.sleep(2)
        clean_text(text, file_name)

# -------------------------
# CLEAN TEXT
# -------------------------
def clean_text(text, file_name):
    """
    Clean and prepare the text:
    - Remove punctuation
    - Convert all text to lowercase
    - Split text into words
    """
    cleaned_text = text
    for p in string.punctuation:
        cleaned_text = cleaned_text.replace(p, "")
    
    lowered_text = cleaned_text.lower()
    words_list = lowered_text.split()
    
    detect_numbers(words_list, file_name)

# ------------------------------
# DETECT NUMBERS
# ------------------------------
def detect_numbers(words_list, file_name):
    """Extract numeric words (e.g., '100', '2024') from the text."""
    numbers_list = [int(word) for word in words_list if word.isdigit()]
    analyze_text(words_list, numbers_list, file_name)

# ------------------------
# ANALYZE TEXT
# ------------------------
def analyze_text(words_list, numbers_list, file_name):
    """
    Analyze text content:
    - Count total and unique words
    - Identify numbers and their counts
    - Determine most common words
    """
    total_words = len(words_list)
    total_numbers = len(numbers_list)
    unique_words = set(words_list)
    unique_numbers = set(numbers_list)
    
    word_frequency = {}
    for word in words_list:
    	if word in word_frequency:
    		word_frequency[word] += 1
    	else:
    		word_frequency[word] = 1
    	
    
    sorted_word_freq = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)
    
    if total_words < 50:
        most_common_words = dict(sorted_word_freq[:2])
    elif total_words < 200:
        most_common_words = dict(sorted_word_freq[:5])
    else:
        most_common_words = dict(sorted_word_freq[:10])
    
    # --- Display quick report ---
    print(f"Total words: {total_words} ({total_numbers} numbers).")
    print(f"Unique words: {len(unique_words)} ({len(unique_numbers)} numbers).")
    print("Most common words:")
    for index, (word, count) in enumerate(most_common_words.items(), start=1):
        print(f"{index}. {word} – {count}")
    print()
    
    save_report(total_words, len(unique_words), most_common_words, total_numbers, len(unique_numbers), file_name)

# ----------------------
# SAVE REPORT
# ----------------------
def save_report(total_words, total_unique_words, most_common_words, total_numbers, total_unique_numbers, file_name):
    """Save the analyzed report into a JSON file."""
    try:
        with open("Word_Report.json", "r") as reports_file:
            word_reports = json.load(reports_file)
    except (FileNotFoundError, json.JSONDecodeError):
        word_reports = []
    
    report = {
        "File name": file_name,
        "Total words": f"{total_words} ({total_numbers} numbers)",
        "Unique words": f"{total_unique_words} ({total_unique_numbers} numbers)",
        "Most common words": [{"Word": w, "Count": c} for w, c in most_common_words.items()]
    }
    
    word_reports.append(report)
    
    with open("Word_Report.json", "w") as reports_file:
        json.dump(word_reports, reports_file, indent=4)
    print("\nReport saved to Word_Report.json\n")

# ------------------------
# VIEW REPORTS
# ------------------------
def view_reports():
    """Display all saved text analysis reports."""
    try:
        with open("Word_Report.json", "r") as report_file:
            reports = json.load(report_file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("\nNo reports found or file unreadable.\n")
        return
    
    if not reports:
        print("\nNo saved reports.\n")
        return
    
    print("\n––– Saved Reports –––\n")
    for index, report in enumerate(reports, start=1):
        print(f"{index}. {report['File name']}")
    
    try:
        choice = int(input(f"\nSelect report (1-{len(reports)}): "))
    except ValueError:
        print("\nInvalid input. Must be a number.\n")
        return
    
    if not (1 <= choice <= len(reports)):
        print("\nChoice out of range.\n")
        return
    
    selected = reports[choice - 1]
    print(f"\nFile name: {selected['File name']}")
    print(f"Total words: {selected['Total words']}")
    print(f"Unique words: {selected['Unique words']}")
    print("Most common words:")
    for index, item in enumerate(selected["Most common words"], start=1):
        print(f"{index}. {item['Word']} – {item['Count']}")
    print()

# ---------------------------
# CLEAR REPORTS
# ---------------------------
def clear_reports():
    """Clear all saved text analysis reports."""
    with open("Word_Report.json", "w") as report_file:
        json.dump([], report_file)
    print("\nAll reports cleared.\n")

# --------------------
# MAIN MENU
# --------------------
while True:
    print("=== Word Miner ===")
    print("1. Analyze Text File")
    print("2. View Reports")
    print("3. Clear Reports")
    print("0. Exit")
    
    try:
        user_option = int(input("\nEnter your choice: "))
    except ValueError:
        print("\nInvalid input. Please enter a number (0–3).\n")
        continue
    
    if user_option == 0:
        print("\nThanks for using Word Miner. Goodbye!")
        break
    elif user_option == 1:
        take_file()
    elif user_option == 2:
        view_reports()
    elif user_option == 3:
        clear_reports()
    else:
        print("\nInvalid input. Please enter a number between 0–3.\n")
