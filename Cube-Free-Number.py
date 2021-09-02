'''
A cube free number is a number who’s none of the divisor is a cube number 
(A cube number is a cube of a integer like 8 (2 * 2 * 2) , 27 (3 * 3 * 3) ). 
So cube free numbers are 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 17, 18 etc 
(we will consider 1 as cube free). 8, 16, 24, 27, 32 etc are not cube free number. 
So the position of 1 among the cube free numbers is 1, position of 2 is 2, 3 is 3 
and position of 10 is 9. Given a positive number you have to say if its a cube free 
number and if yes then tell its position among cube free numbers.

Input
First line of the test case will be the number of test case T (1 <= T <= 100000) . 
Then T lines follows. On each line you will find a integer number n (1 <= n <= 1000000).

Output
For each input line, print a line containing “Case I: ”, where I is the test case number. 
Then if it is not a cube free number then print “Not Cube Free”. 
Otherwise print its position among the cube free numbers.

Sample Input:
10
1
2
3
4
5
6
7
8
9
10

Sample Output:
Case 1: 1
Case 2: 2
Case 3: 3
Case 4: 4 
Case 5: 5
Case 6: 6
Case 7: 7
Case 8: Not Cube Free
Case 9: 8
Case 10: 9
'''

# Code with Basic Knowledge
'''def is_perfect_cube(numbers):
    count = 0
    position = 0
    for number in numbers:
        count+=1
        number = abs(number) 
        l = round(number ** (1 / 3)) ** 3
        if l != number or l == 1:
            print("Case {}: {}".format(count, number-position))
        else:
            position+=1
            print("Case {}: Not Cube Free".format(count))
            

if __name__ == '__main__':
    num_of_tests = int(input())
    tests_list = []
    for test in range(num_of_tests):
        num = int(input())
        tests_list.append(num)
    # tests_list = [25,26,27,28,29]
    is_perfect_cube(tests_list)  '''


# Correct Implementation
size = 1000001
a = [1]*size
def CheckCubeFreeNo():
    a[0]=0
    
    for i in range(2,size):
        if(a[i]==1):
            if(i<=100):
                a[i*i*i]=0
        elif(a[i]==0):
            j = i*2
            while(j<size):
                a[j]=-1
                j=j+i
    a[1] = 1
    previous = a[1]
    for i in range(2,size):
        if(a[i]==1):
            a[i] = previous+1
            previous = a[i]
            
if __name__ == '_main_':
    t = int(input())
    CheckCubeFreeNo()
    for i in range(0,t):
        n = int(input())
        if(a[n]>=1):
            print("Case "+str(i+1)+": "+str(a[n]))
        else:
            print("Case "+str(i+1)+": Not Cube Free")