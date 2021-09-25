st = "(1 1) (8 8)"
k = [int(x) for x in st if x.isnumeric()]
knightpos = k[0:2]
targetpos = k[2:4]
print(knightpos,targetpos)