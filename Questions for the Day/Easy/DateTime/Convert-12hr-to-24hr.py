
s = '07:05:45PM'

time_split = s.split(":")
print(time_split)
if 'PM' in time_split[2]:
    print("PM", time_split[2])
else:
    print("AM", time_split[2])