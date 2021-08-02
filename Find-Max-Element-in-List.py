numbers = [55, 4, 92, 1, 104, 64, 73, 99, 20]

maxnumber = None
for num in numbers:
    if maxnumber is None or num > maxnumber:
        maxnumber = num
print(maxnumber)