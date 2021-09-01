def is_perfect_cube(number):
    """
    Indicates (with True/False) if the provided number is a perfect cube.
    """
    number = abs(number)  # Prevents errors due to negative numbers
    return round(number ** (1 / 3)) ** 3 == number

result = is_perfect_cube(8)
print(result)