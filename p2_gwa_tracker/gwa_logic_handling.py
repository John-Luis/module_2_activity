import os

class GWAProcessor:
    def __init__(self, filename):
        self.filename = filename

    def get_top_student(self):

        if not os.path.exists(self.filename):
            return "File does not exist or missing", 0.0 ,0

        # instead of using lists, i used a dict.. so it is more organized and usable.
        top_student= {"name": "None", "gwa": 5.0}
        processed_total = 0

        # Direct stream processing
        with open(self.filename, 'r') as student_data:
            for current_row in student_data:
                # Clean the line
                entry = current_row.strip()

                # Guard clause to skip empty space
                if not entry:
                    continue

                # Parse data
                info = entry.rsplit(' ', 1)
                full_name = info[0]
                current_gwa = float(info[1])
                processed_total += 1

                # Update winner if current GWA is better (lower)
                if current_gwa < top_student["gwa"]:
                    top_student["name"] = full_name
                    top_student["gwa"] = current_gwa

        return top_student["name"], top_student["gwa"], processed_total