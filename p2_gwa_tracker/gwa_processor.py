import time
import os
from gwa_logic_handling import gwa_logic as gwa_function

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

    print(f"{CYAN}{'=' * 55}{RESET}")
    print(f"{BOLD}{WHITE}   OFFICIAL STUDENT GWA TRACKER - ACADEMIC YEAR 2026{RESET}")
    print(f"{CYAN}{'=' * 55}{RESET}")

    # Simple Loading Bar that i found in the internet
    for i in range(1, 11):
        print(f"\rProcessing: [{'█' * i}{'░' * (10 - i)}]", end="")
        time.sleep(0.1)