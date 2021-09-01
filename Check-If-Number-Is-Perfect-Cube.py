def is_perfect_cube(num):

    num = abs(num)
    return round(num ** (1 / 3)) ** 3 == num

result = is_perfect_cube(8)
print(result)