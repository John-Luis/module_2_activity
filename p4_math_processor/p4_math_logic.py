# math_logic.py
import os

class MathEngine:
    def __init__(self, target_file):
        # We removed the hardcoded "integers.txt"
        self.target_file = target_file
        self.CYAN = '\033[96m'
        self.GREEN = '\033[92m'
        self.RESET = '\033[0m'      