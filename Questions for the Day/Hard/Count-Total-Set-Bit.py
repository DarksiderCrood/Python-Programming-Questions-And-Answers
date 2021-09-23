#User function Template for python3

class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    def countSetBits(self,n):
        # code here
        # return the count
        count=0
        i=1
        
        while(i<=n):
           i=i*2
           q=(n+1)//i
           r=(n+1)%i
           t=q*(i//2)
           
           if r>(i//2):
               t+=r-i//2
           count+=t
        return count
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        ob=Solution()
        print(ob.countSetBits(int(input())))
# } Driver Code Ends