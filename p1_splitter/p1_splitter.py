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