
s = '12:05:45AM'

time_split = s.split(":")
print(time_split)
if 'PM' in time_split[2]:
    #print("PM", time_split[2])
    if int(time_split[0]) < 12:
        hr = int(time_split[0])+12
        print(str(hr)+":"+time_split[1]+":"+time_split[2].replace('PM',''))
    else:
        print(time_split[0]+":"+time_split[1]+":"+time_split[2].replace('PM',''))

else:
    #print("AM", time_split[2])
    if int(time_split[0]) < 12:
        print(time_split[0]+":"+time_split[1]+":"+time_split[2].replace('AM',''))
    else:
        hr = int(time_split[0])-12
        print(str(hr)+":"+time_split[1]+":"+time_split[2].replace('AM',''))