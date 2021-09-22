# Find Subs of A
def A_Subs(A):
    # code here
    count = 1
    while True:
        if B in A:
            return count
            break
        else:
            count+=1
            A = A+A
    return -1

# Other Approach
'''
    def repeatedStringMatch(self, A, B):
        num=A
        if A.count(B)>0:
            return 1
        else:
            count=1
            while( len(A)<len(B)):
                A+=num
                count+=1
            if A.count(B)>0:
                return count
            A+=num
            count+=1
            if A.count(B)>0:
                return count
        return -1
'''


# Main
if __name__ == '__main__':
    # Inputs
    A = "abcd"
    B = "cdabcdab"
    result = A_Subs(A)
    print(result)


