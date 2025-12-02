# src/__main__.py

import argparse
from src.calculator import add, subtract, multiply, divide

def main():
    parser = argparse.ArgumentParser(description="A simple CLI calculator.")
    parser.add_argument("num1", type=float, help="The first number")
    parser.add_argument("operator", type=str, help="The operator (+, -, *, /)")
    parser.add_argument("num2", type=float, help="The second number")

    args = parser.parse_args()

    try:
        if args.operator == '+':
            result = add(args.num1, args.num2)
        elif args.operator == '-':
            result = subtract(args.num1, args.num2)
        elif args.operator == '*':
            result = multiply(args.num1, args.num2)
        elif args.operator == '/':
            result = divide(args.num1, args.num2)
        else:
            print(f"Error: Unsupported operator '{args.operator}'")
            return

        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
