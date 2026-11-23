"""Complete this function for the SCCM4910 coursework.

Place this file beside your existing lab calculator.py. The runner and
file handling are supplied; write your own processing logic and tests.
"""

import math
from calculator import add, subtract, multiply, divide


def process_calculation(operation, a_text, b_text):

    operation = operation.strip()

    if operation not in ("add", "subtract", "multiply", "divide"):
        return ("ERROR", "", "UNKNOWN_OPERATION")

    a_text = a_text.strip()
    b_text = b_text.strip()

    try:
        numa = float(a_text)
    except ValueError:
        return ("ERROR", "", "INVALID_NUMBER")

    try:
        numb = float(b_text)
    except ValueError:
        return ("ERROR", "", "INVALID_NUMBER")

    # Check for non-finite numbers
    if not math.isfinite(numa) or not math.isfinite(numb):
        return ("ERROR", "", "INVALID_NUMBER")

    # Check number range
    if numa > 1000 or numa < -1000 or numb > 1000 or numb < -1000:
        return ("ERROR", "", "INVALID_NUMBER")

    # Check ordinary decimal notation
    if not a_text.replace(".", "", 1).replace("-", "", 1).isdigit():
        return ("ERROR", "", "INVALID_NUMBER")

    if not b_text.replace(".", "", 1).replace("-", "", 1).isdigit():
        return ("ERROR", "", "INVALID_NUMBER")

    # Split decimal portions
    a_parts = a_text.split(".")
    b_parts = b_text.split(".")

    # Check decimal precision
    if len(a_parts) == 2 and len(a_parts[1]) > 3:
        return ("ERROR", "", "INVALID_NUMBER")

    if len(b_parts) == 2 and len(b_parts[1]) > 3:
        return ("ERROR", "", "INVALID_NUMBER")

    #Check for division by zero
    if operation == "divide" and numb == 0:
        return ("ERROR", "", "DIVISION_BY_ZERO")

    #Perform the arithmetic
    if operation == "add":
        result = add(numa, numb)
    elif operation == "subtract":
        result = subtract(numa, numb)
    elif operation == "multiply":
        result = multiply(numa, numb)
    elif operation == "divide":
        result = divide(numa, numb)

    #Return the result
    return ("OK", result, "")


