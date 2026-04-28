from p4_math_logic import MathEngine

def main():
    processor = MathEngine('integers.txt')

    processor.run_engine()
    processor.print_summary()

if __name__ == "__main__":
    main()