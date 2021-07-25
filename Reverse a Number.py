num = int(input("Enter the number: "))
li = [x for x in str(num)]
print("".join(li[::-1]))