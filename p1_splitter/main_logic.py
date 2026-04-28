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

    def process_data(self):
        self._header("DATA PROCESSING")
        evens = []
        odds = []

        # Manual file existence check
        if not os.path.exists(self.input_file):
            print("⚠️ numbers.txt missing. Generating...")
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

# Add to separator_logic.py
    def export_results(self, evens, odds):
        self._header("SAVING ARCHIVES")

        # Writing Even File
        e_file = open('even_numbers.txt', 'w')
        for n in evens:
            e_file.write(str(n) + "\n")
        e_file.close()

        # Writing Odd File
        o_file = open('odd_numbers.txt', 'w')
        for n in odds:
            o_file.write(str(n) + "\n")
        o_file.close()

        print(f"even_numbers.txt created | odd_numbers.txt created")

    def show_summary(self):
        self._header("ARCHIVE SUMMARY")

        print(f"{self.GREEN}[ EVEN ARCHIVE ]{self.RESET}")
        e_file = open('even_numbers.txt', 'r')
        even_content = e_file.read().strip().replace('\n', ', ')
        print(even_content if even_content else "No data.")
        e_file.close()

        print("\n" + "-" * 40)


        print(f"{self.GREEN}[ ODD ARCHIVE ]{self.RESET}")
        o_file = open('odd_numbers.txt', 'r')
        odd_content = o_file.read().strip().replace('\n', ', ')
        print(odd_content if odd_content else "No data.")
        o_file.close()

        print(f"\n{self.CYAN}{'=' * 40}{self.RESET}")

