inputStr = list(input().split())
digit = input()

result =""
for i in range(len(inputStr)):
    if(inputStr[i].count(digit)>0):
        result+=inputStr[i].replace(digit,"")+" "
    else:
        result+=inputStr[i]+" "

print(result)
