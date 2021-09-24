'''
Question:
    Given string s, let s[i] represent the th character in the string s, using O-based indexing.

    1. Initially i = 0. 
    2. If s[i] is lowercase and the next character
        S[i+1] is uppercase, swap them, add a '*' after them, and move to i+2. 
    3. If s[i] is a number, replace it with 0. place
        the original number at the start, and move to 1+1 
    4. Else, move to i+1. 
    5. Stop if i is more than or equal to the string length. Otherwise, go to step 2.


    There's even an example mentioned in the notebook. When encrypted, 
    the string "hAck3rr4nk" becomes "43Ah*ckOrronk" (Note: the original string, "hAck3rr4nk", 
    does not contain the character 0.)

Note:
    • The original string always contains digits
        from 1 to 9 and does not contain 0. 
    • The original string always contains only
        alpha-numeric characters.

Sample Input For Custom Testing:
    51Pa*OLp De

Sample Output:
    aPlpL5e

Explanation:
    If we apply the sequence of operations on the string aP1pL5e, we get the string 51Pa*OLp*0e.
    1. We start at the letter a since i = 0. 
    2. Since a is lowercase and the next character P is uppercase, we swap them, 
        add a '*' after, and move to the next designated character (1+2). So currently it is Pa*1pL5e. 
    3. Now we're on the character 1. This is a number, so we replace it with o, put the original number 
        1 at the start, and continue to the next character (i+1). Now it is 1Pa*OpL5e. 
    4. We're still in the middle of the string (i does not equal the string length), 
        so we repeat the process again. 
    
    After that, 1Pa*OpL5e becomes 1Pa*OLp*5e. 
    Then, 1Pa*OLp*5e becomes 51 Pa*OLp*0e. Since e is at the end of the string, 
    it can't be swapped with the next character. Thus, ap1pL5e becomes 51 PakOLp*oe when encrypted.
'''


# Output: hAck3rr4nk Input: 43Ah*ck0rr0nk
# Output: poTaTO Input: pTo*Ta*O
s = "poTaTO" # Output: aP1pL5e Input: 51Pa*0Lp*0e
l = [x for x in s]
pos = []
ad = []

for x in range(0, len(l)):
    if x < len(l)-1:
        if l[x].islower() and l[x+1].isupper():
            l[x], l[x+1] = l[x+1], l[x]
            pos.append(x+1+1)
pos_inc = 0
for i in pos:
    l.insert(i+pos_inc, '*')
    pos_inc+=1
# print(''.join(l))

for x in range(0,len(l)):
    if x < len(l)-1:
        if l[x].isnumeric():
            ad.append(l[x])
            l[x] = '0'
p3 = ad[::-1]+l 
print(''.join(p3))



