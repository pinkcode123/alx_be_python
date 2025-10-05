# main.py
import sys
from robust_division_calculator import safe_divide

def main():
    # Check if user gave exactly 2 arguments
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Call your safe_divide function
    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()