import os
from datetime import datetime

class LifeVault:
    def __init__(self, target_name):
        self.target_name = target_name
        self.vault = []
        self.today = datetime.now().strftime("%B %d, %Y")

    def add_line(self, text):
        # Basic addition to the buffer
        self.vault.append(text)

    def finalize(self):
        # Write the buffer to the file
        with open(self.target_name, "a") as f:
            f.write("\n".join(self.vault) + "\n")