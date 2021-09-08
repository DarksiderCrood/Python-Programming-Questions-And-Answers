a = 2
b = 3
x = 10
y = 20
# Without Using Temporary Variable
a, b = b, a
print(a, b)

# Addition and Subtraction
x = x + y
y = x - y
x = x - y
print(x, y)

# XOR swap
# This algorithm works for integers only
x = x ^ y
y = x ^ y
x = x ^ y
print(x, y)

# Multiplication and Division
x = x * y
y = x / y
x = x / y
print(x, y)