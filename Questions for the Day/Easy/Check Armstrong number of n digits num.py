# Armstrong number is a number that is equal to the sum of cubes of its digits.
"""
# Check Armstrong number of n digits
# Armstrong number is a number that is equal to the sum of cubes of its digits
num = int(input("Enter the number: "))

# Changed num variable to string,
# and calculated the length (number of digits)
order = len(str(num))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** order
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
"""


# With For loop
num = int(input("Enter the number: "))
temp = str(num)
pow = len(str(num))
sum = 0
# print("Your Number is {} and Its Lenght is {}".format(num,pow))
if num < 0:
 print("Please enter positive value")
else:
 for x in temp:
  k = int(x)
  sum = sum + k ** pow

if num == sum:
 print("{} is an armstrong numbner".format(num))
else:
 print("{} is not an armstrong number".format(num))
