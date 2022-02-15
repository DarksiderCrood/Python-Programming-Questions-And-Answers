def remAnagram(str1,str2):
    
    #add code here
    if len(str1) > len(str2):
        count = 0
        for x in str2:
            if not x in str1:
                count +=1
        print(count)
    else:
        for x in str1:
            if not x in str2:
                count +=1
        print(count)

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        str2=input()
        print(remAnagram(str1,str2))
# } Driver Code Ends