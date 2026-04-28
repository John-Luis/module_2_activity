import os

class GWAProcessor:
    def __init__(self, filename):
        self.filename = filename

    def get_top_student(self):

        if not os.path.exists(self.filename):
            return "File does not exist or missing", 0.0 ,0

        top_name = "None"
        best_grade = 5.0
        cleaned_lines = []

        with open(self.filename, "r") as file:
            for line in file:
                stripped_line = line.strip()

                if stripped_line:
                    cleaned_lines.append(stripped_line)