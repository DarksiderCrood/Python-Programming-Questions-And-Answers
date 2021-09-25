from itertools import islice


s = "poTaTO" # pTo*Ta*O
l = [x for x in s]
lines = list(s)
lit = iter(enumerate(lines))
pos = []
ad = []

for x in range(0, len(l)):
    if x < len(l)-1:
        if l[x].islower() and l[x+1].isupper():
            l[x], l[x+1] = l[x+1], l[x]
            pos.append(x+1+1)
            next(islice(l, 2), None)

pos_inc = 0
for i in pos:
    l.insert(i+pos_inc, '*')
    pos_inc+=1
print(''.join(l))