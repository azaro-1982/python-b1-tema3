# geometry.py
import math
def square_area(side_length: float) -> float:
    """
    Calculate the area of a square.

    Args:
    - side_length (float): the length of one side of the square.

    Returns:
    - float: the area of the square.
    """
    # Write here your code
    area = side_length * side_length
    return area


def rectangle_area(base_length: float, height: float) -> float:
    """
    Calculate the area of a rectangle.

    Args:
    - base_length (float): the length of the base of the rectangle.
    - height (float): the height of the rectangle.

    Returns:
    - float: the area of the rectangle.
    """
    # Write here your code
    area = base_length * height
    return area


def triangle_area(base_length: float, height: float) -> float:
    """
    Calculate the area of a triangle.

    Args:
    - base_length (float): the length of the base of the triangle.
    - height (float): the height of the triangle.

    Returns:
    - float: the area of the triangle.
    """
    # Write here your code
    area = (base_length * height) / 2
    return area


def circle_area(radius: float) -> float:
    """
    Calculate the area of a circle.

    Args:
    - radius (float): the radius of the circle.

    Returns:
    - float: the area of the circle
    """
    # Write here your code
    if not isinstance(radius, (int, float)):
        raise TypeError("El valor debe ser un valor numérico")
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    
    area = math.pi * (radius**2)
    return area
