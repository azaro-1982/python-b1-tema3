# archivo ej3a1_operations.py


def add(num_1: float, num_2: float) -> float:
    # Write here your code
    return num_1 + num_2


def subtract(num_1: float, num_2: float) -> float:
    # Write here your code
    return num_1 - num_2


def multiply(num_1: float, num_2: float) -> float:
    # Write here your code
    return num_1 * num_2


def divide(num_1: float, num_2: float) -> float:
    # Write here your code
    if num_2 == 0:
        raise ZeroDivisionError("No se puede dividir por 0")
    return num_1 / num_2
