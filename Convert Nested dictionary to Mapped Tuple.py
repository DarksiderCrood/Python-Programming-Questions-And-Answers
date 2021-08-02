inp = {'A' : {'a' : 'dfd', 'b' : 'frvr'}, 'B' : {'a' : 'erv', 'b' : 'fwv'},'C' : {'a' : 'ewv', 'b' : 'wf'}}

ans = []
l = list(inp.keys())
for key in inp[l[0]]:
    temp=[]
    for subDict in inp.values():
        temp.append(subDict[key])
    ans.append((key,tuple(temp)))

print(ans)