# math_logic.py
import os

class MathEngine:
    def __init__(self, target_file):
        # We removed the hardcoded "integers.txt"
        self.target_file = target_file
        self.CYAN = '\033[96m'
        self.GREEN = '\033[92m'
        self.RESET = '\033[0m'

    def _get_numbers(self):
        nums = []
        file = open(self.target_file, 'r')
        content = file.read()  # Read everything as one string
        file.close()

        # Split by comma OR whitespace, then convert to int
        raw_data = content.replace(',', ' ').split()
        for item in raw_data:
            nums.append(int(item))
        return nums

    def run_engine(self):
        print(f"{self.CYAN}--- STARTING MATH ENGINE ---{self.RESET}")
        data = self._get_numbers()
        
        d_file = open('double.txt', 'w')
        t_file = open('triple.txt', 'w')

        for n in data:
            if n % 2 == 0:
                # Square even numbers
                d_file.write(str(n ** 2) + "\n")
            else:
                # Cube odd numbers
                t_file.write(str(n ** 3) + "\n")

        d_file.close()
        t_file.close()
        print(f"{self.GREEN}✔️ double.txt and triple.txt generated.{self.RESET}")