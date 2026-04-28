# app.py
from main_logic import EvenOddSeparator


def run():
    engine = EvenOddSeparator('.txt')

    # 1. Sort the numbers
    evens, odds = engine.process_data()

    # 2. Save them to files
    engine.export_results(evens, odds)

    # 3. New: View the summary
    engine.show_summary()

    print("\n\033[1m[ SYSTEM SECURED & COMPLETE ]\033[0m")


if __name__ == "__main__":
    run()