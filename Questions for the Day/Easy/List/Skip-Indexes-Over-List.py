from itertools import islice

mods = list("DarkSider Crood")

emu = iter(enumerate(mods))
for x, y in emu:
    print(x, y)
    if y == "r":
        next(islice(emu, 3,3), None)