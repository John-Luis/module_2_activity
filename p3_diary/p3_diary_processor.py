import time
import os
from p3_diary_logic import LifeVault

def start_session():
    CONSOLE_BAR = "\033[97m\033[40m"
    CYAN, YELLOW, BOLD, RESET = "\033[96m", "\033[93m", "\033[1m", "\033[0m"

    manager = LifeVault("mylife.txt")
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"{CONSOLE_BAR}{BOLD}  SYSTEM BOOT: {manager.today.upper()}  {RESET}\n")

 