# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Tries to convert numerator and denominator to floats and perform division.
    Returns a result message or an error message if input invalid or division by zero.
    """
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = num / den  # using Python true division => returns float when appropriate :contentReference[oaicite:0]{index=0}
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    return f"The result of the division is {result}"
