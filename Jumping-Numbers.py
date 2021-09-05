'''Print all Jumping Numbers smaller than or equal to a given value
A number is called as a Jumping Number if all adjacent digits in it differ by 1. 
The difference between ‘9’ and ‘0’ is not considered as 1. 
All single digit numbers are considered as Jumping Numbers. 

For example 7, 8987 and 4343456 are Jumping numbers but 796 and 89098 are not. 
Given a positive number x, print all Jumping Numbers smaller than or equal to x. 
The numbers can be printed in any order.

Example: 

Input: x = 20
Output:  0 1 2 3 4 5 6 7 8 9 10 12

Input: x = 105
Output:  0 1 2 3 4 5 6 7 8 9 10 12
         21 23 32 34 43 45 54 56 65
         67 76 78 87 89 98 101

Note: Order of output doesn't matter, 
i.e. numbers can be printed in any order'''

num = 20

n_str = []
jumping_nums = []
original_nums = [x for x in range(0,20+1)]
more_digits_nums = []

for x in range(0, 20+1):
    n_str.append(''.join(sorted(str(x), reverse=False)))
    
for y in n_str:
    if len(y) == 1:
        jumping_nums.append(True)
    else:
        jumping_nums.append(y)

for z in jumping_nums:
    if z:
        continue
    else:
        for f in range(0,len(z)):
            try:
                if int(z[f])+1 == int(z[f+1]) or int(z[f]) == int(z[f+1]):
                    jumping_nums.append(True)
            except:
                continue

print(original_nums)
print(jumping_nums)

