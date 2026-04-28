import os
from datetime import datetime

class LifeVault:
    def __init__(self, target_name):
        self.target_name = target_name
        self.vault = []
        # Adding the maangas timestamp [MONTH:DAY:YEAR]
        self.today = datetime.now().strftime("%B %d, %Y")

    def add_line(self, text):
        # Adding the maangas timestamp [HH:MM:SS]
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.vault.append(f"[{timestamp}] {text}")

    def finalize(self):
        with open(self.target_name, "a") as f:
            # Adds a visual header for the date
            f.write(f"\n--- LOG ENTRY: {self.today} ---\n")
            f.write("\n".join(self.vault) + "\n")