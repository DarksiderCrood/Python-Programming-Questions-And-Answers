'''
Given a positive integer 'n', find and return the minimum number of steps that 'n' 
has to take to get reduced to 1. You can perform any one of the following 3 steps:
    1.) Subtract 1 from it. (n = n - ­1)
    2.) If its divisible by 2, divide by 2.( if n % 2 == 0, then n = n / 2 )
    3.) If its divisible by 3, divide by 3. (if n % 3 == 0, then n = n / 3 )  

Sample Input 1 :
    4

Sample Output 1 :
    2 

Explanation of Sample Output 1 :
    For n = 4
    Step 1 :  n = 4 / 2  = 2
    Step 2 : n = 2 / 2  =  1
'''


def minimum_steps(num):
    if num == 1:
        return 0
    
    step = 0

    while num > 1:
        step = step + 1
        if  num % 2 == 0:
            num = num / 2
        elif num % 3 == 0:
            num = num /3
        else:
            num = num -1
    return step

if __name__ == '__main__':
    num = int(input("\nEnter Positive Integer: "))
    result = minimum_steps(num)
    print("Minimum Steps: {}\n".format(result))