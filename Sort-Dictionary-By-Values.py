dt = {'a':4,'b':1,'c':8,'d':2}
sorted_dt = {key: value for key, value in sorted(dt.items(), key=lambda item: item[1])}

print(sorted_dt)
