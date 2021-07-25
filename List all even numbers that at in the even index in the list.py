lis = [1, 3, 5, 8, 10, 13, 18, 36, 78]
print(lis[::-1])
print(lis[::1])
print(lis[::2])
print(lis[::3])

print([a for a in lis[::2] if a % 2 == 0])

