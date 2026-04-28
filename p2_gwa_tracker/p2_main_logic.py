import os

class gwa_logic:
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

                entry = current_row.strip()

                if not entry:
                    continue

                # Parse data
                info = entry.rsplit(' ', 1)
                full_name = info[0]
                current_gwa = float(info[1])
                processed_total += 1

                # Update top_student if current GWA is better (lower)
                if current_gwa < top_student["gwa"]:
                    top_student["name"] = full_name
                    top_student["gwa"] = current_gwa

        return top_student["name"], top_student["gwa"], processed_total

    def get_full_registry(self):
        all_students = []
        if not os.path.exists(self.filename):
            return []

        def get_gwa_value(student_dict):
            return student_dict["GWA"]

        with open(self.filename, 'r') as student_data:
            for current_row in student_data:
                entry = current_row.strip()
                if not entry: continue

                info = entry.rsplit(' ', 1)
                all_students.append({
                    "STUDENT NAME": info[0].upper(),
                    "GWA": float(info[1])
                })

        return sorted(all_students, key=get_gwa_value)