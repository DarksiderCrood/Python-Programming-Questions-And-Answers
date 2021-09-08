# inputStr = list(input().split())
# per = int(input())
# result = ""
# for i in range(len(inputStr)):
#     num = int((per/100)*len(inputStr[i]))
#     str1 = inputStr[i][:num]
#     str2 = inputStr[i][num:]
#     result+= str1+" "+str2+" "
# print(result)


st = 'live like a hell to keep yourself evolving'
split = 50
print("Splite Result : {}\n".format(' '.join([ele[:int((split/100) * len(ele))] + " " + ele[int((split/100) * len(ele)):] for ele in st.split()])))
