'''
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome. 
The string will only contain lowercase characters a-z.

Test case:
    string = 'radkar'
    output = True
'''

class Palindrome:
    def __init__(self, st):
        self.string = st
    
    def palin(self):
        li = [x for x in self.string]
        for x in range(0, len(li)):
            mem = li[x]
            del li[x]
            check = ''.join(li)
            if check == check[::-1]:
                return 1
            li.insert(x, mem)
        return -1


if __name__ == '__main__':
    str = 'nitin'
    pal1 = Palindrome(str)
    result = pal1.palin()
    if result == 1:
        print("It's a Palindrome")
    else:
        print("Not a Palindrome")