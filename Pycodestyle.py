#!/usr/bin/python3

# Import statements should be at the top of the file.

import math
import datetime

# Use clear and descriptive variable and function names.
def calculate_circle_area(radius):
    """
    Calculate the area of a circle.
    
    Args:
        radius (float): The radius of the circle.
    
    Returns:
        float: The area of the circle.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    
    # Use a space after the comma in function arguments.
    return math.pi * radius ** 2

# Use two blank lines to separate functions and classes.
class Person:
    def __init__(self, first_name, last_name, birthdate):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
    
    def calculate_age(self):
        """
        Calculate the age of the person.
        
        Returns:
            int: The age of the person.
        """
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        
        # Use a space around operators.
        if today.month < self.birthdate.month or (today.month == self.birthdate.month and today.day < self.birthdate.day):
            age -= 1
        
        return age

# Indentation should be 4 spaces per level.
if __name__ == "__main__":
    # Use a blank line before and after control structures.
    print("Enter the radius of the circle:")
    radius = float(input())
    
    # Use consistent indentation (4 spaces) for blocks.
    area = calculate_circle_area(radius)
    
    # Use f-strings for string formatting.
    print(f"The area of the circle is: {area:.2f}")
