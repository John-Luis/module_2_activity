# separator_logic.py
import os

class EvenOddSeparator:
    def __init__(self, input_file):
        self.input_file = input_file
        # ANSI Colors for that 'maangas' look
        self.CYAN = '\033[96m'
        self.GREEN = '\033[92m'
        self.YELLOW = '\033[93m'
        self.RESET = '\033[0m'

    def _header(self, text):
        print(f"\n{self.CYAN}{'='*45}")
        print(f" {text.center(43)}")
        print(f"{'='*45}{self.RESET}")

    def check_and_load(self):
        self._header("CORE ENGINE: DATA ANALYSIS")
        if not os.path.exists(self.input_file):
            print(f"{self.YELLOW}[!] {self.input_file} missing. Generating sample...{self.RESET}")
            with open(self.input_file, 'w') as f:
                f.write("10\n21\n32\n43\n54\n65")
        return True

    def _header(self, text):
        print(f"\n{self.CYAN}{'='*45}")
        print(f" {text.center(43)}")
        print(f"{'='*45}{self.RESET}")


def process_data(self):
    self._header("DATA PROCESSING")
    evens = []
    odds = []

    # Manual file existence check
    if not os.path.exists(self.input_file):
        print("numbers.txt missing. Generating...")
        temp = open(self.input_file, 'w')
        temp.write("10\n15\n20\n25\n30")
        temp.close()

    # MANUAL OPEN AND CLOSE
    file = open(self.input_file, 'r')
    for line in file:
        line = line.strip()
        if line:
            num = int(line)
            if num % 2 == 0:
                evens.append(num)
            else:
                odds.append(num)
    file.close()  # <--- CRITICAL: Manual closing

    print(f"{self.GREEN} Processed {len(evens) + len(odds)} items.{self.RESET}")
    return evens, odds
