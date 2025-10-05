# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Convert inputs to numbers
        num = float(numerator)
        den = float(denominator)

        # Try to divide
        result = num / den
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        # This happens when denominator is 0
        return "Error: Cannot divide by zero."

    except ValueError:
        # This happens when user enters text like "ten"
        return "Error: Please enter numeric values only."