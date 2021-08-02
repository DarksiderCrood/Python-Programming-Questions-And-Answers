# Methode 1 (Not Comepleted)
inp_list = [4, 3, 5, 6]

lenght = len(inp_list)
l1 = []
l2 = []

for ele in inp_list:
    ind = inp_list.index(ele)
    inp_list.remove(ele)
    l1.append(ele)
    sum1 = sum(l1)
    l1 = []
    sum2 = sum(inp_list)
    inp_list.insert(ind, ele)
    print(sum1, sum2)
    if sum1>sum2:
        l2.append(sum1-sum2)
    else:
        l2.append(sum2-sum1)
print(min(l2))

