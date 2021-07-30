inputStr = list(input().split())
per = int(input())

result = ""
for i in range(len(inputStr)):
    num = int((per/100)*len(inputStr[i]))
    str1 = inputStr[i][:num]
    str2 = inputStr[i][num:]
    result+= str1+" "+str2+" "

print(result)