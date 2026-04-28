import time

manager = LifeVault("mylife.txt")
os.system('cls' if os.name == 'nt' else 'clear')

print(f"{CONSOLE_BAR}{BOLD}  SYSTEM BOOT: {manager.today.upper()}  {RESET}\n")

manager = LifeVault("mylife.txt")
os.system('cls' if os.name == 'nt' else 'clear')    

print(f"{CONSOLE_BAR}{BOLD}  SYSTEM BOOT: {manager.today.upper()}  {RESET}\n")