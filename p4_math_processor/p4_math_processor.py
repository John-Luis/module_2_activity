# app.py
from p4_math_logic import MathEngine


def main():
    # Pass the filename here instead of inside the class
    processor = MathEngine('integers.txt')

    processor.run_engine()
    processor.print_summary()


if __name__ == "__main__":
    main()