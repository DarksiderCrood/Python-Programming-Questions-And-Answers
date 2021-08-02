# Methode 1
print("\nMethode 1")
inputStr = 'qweertrty'

result =[0]*26

for i in inputStr:
    result[ord(i)-ord('a')]+=1
tempstr = set(inputStr)
for i in inputStr:
    if(i in tempstr):
        ans = result[ord(i)-ord('a')]
        print(i+" : "+ str(ans))
        tempstr.remove(i)

# Methode 2
print("\nMethode 2")
str = 'qweertrty'
count_with_dic = {}
for ch in str:
    if ch == ' ':
        continue
    if ch in count_with_dic:
        count_with_dic[ch] += 1
    else:
        count_with_dic[ch] = 1
for k, v in count_with_dic.items():
    print('{} = {}'.format(k,v))

# Methode 3
print("\nMethode 3")
from collections import Counter
str1 = 'qweertrty'
str = Counter(str1)
for k, v in str.items():
    if k == ' ':
        continue
    print('{} | {}'.format(k,v)) 
