import time
import os
from p3_diary_logic import LifeVault

def start_session():
    CONSOLE_BAR = "\033[97m\033[40m"
    CYAN, YELLOW, BOLD, RESET = "\033[96m", "\033[93m", "\033[1m", "\033[0m"

    manager = LifeVault("mylife.txt")
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"{CONSOLE_BAR}{BOLD}SYSTEM BOOT: {manager.today.upper()}{RESET}")
    print(f"{CONSOLE_BAR}{BOLD}Welcome, User! {RESET}\n")

    while True:
        content = input(f"{CYAN}Enter line: {RESET}")
        manager.add_line(content)
        if input(f"{BOLD}Add more? (y/n): {RESET}").lower().strip() == 'n':
            break

    print(f"\n{YELLOW}GENERATING SESSION SUMMARY...{RESET}")
    time.sleep(0.8)

    total = len(manager.vault)
    manager.finalize()

    print(f"{BOLD}{'-' * 40}{RESET}")
    print(f"Total entries recorded: {BOLD}{total}{RESET}")
    print(f"{CONSOLE_BAR}{BOLD}  SUCCESS: SESSION LOGS SECURED  {RESET}\n")

if __name__ == "__main__":
        start_session()

