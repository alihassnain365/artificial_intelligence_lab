def calculator(num1, num2, operation="addition", output_format="floating point"):

    # Check operation
    if operation not in ["addition", "subtraction", "multiplication", "division"]:
        raise ValueError("Invalid arithmetic operation")

    # Check output format
    if output_format not in ["integer", "floating point"]:
        raise ValueError("Invalid output format")

    # Perform operation
    if operation == "addition":
        result = num1 + num2

    elif operation == "subtraction":
        result = num1 - num2

    elif operation == "multiplication":
        result = num1 * num2

    elif operation == "division":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = num1 / num2

    # Convert result to requested format
    if output_format == "integer":
        return round(result)

    return float(result)


# Examples
print(calculator(10, 3))
print(calculator(10, 3, "addition", "integer"))
print(calculator(10, 3, "subtraction"))
print(calculator(10, 3, "multiplication"))
print(calculator(10, 3, "division"))