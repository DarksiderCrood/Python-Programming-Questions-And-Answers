data = [1,2,8,3,12]

largest = None
second_largest = None

for a in data:
    if not largest or a > largest:
        if largest:
            second_largest = largest
        largest = a

print("largest: {}".format(largest))
print("second_largest: {}".format(second_largest))