# Find minimum difference of sum of two list after dividing list into two

inp = [12,13,11,15,10,26,12,200]

inp.sort()
print(inp)

a1 = []
b1 = []
sum_a1 = []
sum_b1 = []

for x in inp[::-1]:
    if x == inp[-1]:
        a1.append(x)
        print(sum(sum_a1))
    else:
        b1.append(x)
        print(sum(sum_b1))



# Find max numer in list
# Find last two max number in list
