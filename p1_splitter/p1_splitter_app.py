# app.py
from main_logic import EvenOddSeparator


def run():
    engine = EvenOddSeparator('random_generated_numbers.txt')

    # Run the steps
    evens, odds = engine.process_data()
    engine.export_results(evens, odds)

    print("\n\033[1m[ SYSTEM SECURED & COMPLETE ]\033[0m")


if __name__ == "__main__":
    run()