def remAnagram(str1,str2):
    
    #add code here
    if len(str1) < len(str2):
        count = 0
        for x in str1:
            if x in str2:
                count +=1
        if count == len(str1):
            return len(str2) - count
    else:
        count = 0
        for x in str2:
            if x in str1:
                count +=1
        if count == len(str2):
            return len(str1) - count

#{ 
#  Driver Code Starts
if __name__=='__main__':
    str1 = 'basgadhbfgvhads'
    str2 = 'sjdhgvbjdsbhvbvd'
    print(remAnagram(str1,str2))
# } Driver Code Ends