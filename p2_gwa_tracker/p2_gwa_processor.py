import time
import os
import sys # for the typewriter font
from p2_main_logic import gwa_logic as gwa_function
import pandas as pd # Import pandas for the DataFrame

def type_text(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()  # Final newline

def start_application():
    # Visual UI Colors
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    WHITE = "\033[97m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    # Using 'gwa_function' since it is the class name for the importing.
    analyzer = gwa_function('students.txt')
    # Refresh the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

    type_text(f"{CYAN}{'=' * 55}{RESET}")
    type_text(f"{BOLD}{WHITE}   OFFICIAL STUDENT GWA TRACKER - ACADEMIC YEAR 2026{RESET}")
    type_text(f"{CYAN}{'=' * 55}{RESET}")

    # Simple Loading Bar that i found in the internet
    for i in range(1, 11):
        print(f"\rProcessing: [{'█' * i}{'░' * (10 - i)}]", end="")
        time.sleep(0.1)

    # Now, executing and using the logic that we created from the other py file/

    name, gwa, total = analyzer.get_top_student()

    # Found a maangas way to code this, using what our EDA professor taught us on his subject. Using the data frame for displaying the top student.
    # By using this, i implemented and created a maangas way of coding, and visual representation.
    # By importing pandas, because the dataframe function is there

    data = {
        "Category": ["Total Scanned", "Highest GWA", "Top Student"],
        "Value": [total, gwa, name.upper()]
    }
    df = pd.DataFrame(data)

    # 2. Display Result
    type_text(f"{GREEN}{BOLD}[DONE] ANALYSIS COMPLETE{RESET}")
    type_text(f"{WHITE}{'-' * 55}{RESET}")

    # We use to_string(index=False) to hide the row numbers (0, 1, 2)
    type_text(df.to_string(index=False))

    type_text(f"{WHITE}{'-' * 55}{RESET}\n")

    #New Section: Full List Registry
    type_text(f"\n{CYAN}[SYSTEM] GENERATING FULL ACADEMIC REGISTRY...{RESET}", 0.04)
    time.sleep(0.5)

    # Get the data and convert to DataFrame
    full_data = analyzer.get_full_registry()
    full_df = pd.DataFrame(full_data)

    print(f"\n{WHITE}{'=' * 55}{RESET}")
    print(f"{BOLD}           COMPLETE STUDENT RANKING{RESET}")
    print(f"{WHITE}{'=' * 55}{RESET}")

    # Display the full dataframe
    if not full_df.empty:
        print(full_df.to_string(index=True)) # index=True shows the rank (0, 1, 2...)
    else:
        print(f"{YELLOW}No records found in database.{RESET}")

    print(f"{WHITE}{'-' * 55}{RESET}")
    type_text(f"{GREEN}Total Registry Count: {len(full_df)} students listed.{RESET}", 0.02)

if __name__ == "__main__":
    start_application()

