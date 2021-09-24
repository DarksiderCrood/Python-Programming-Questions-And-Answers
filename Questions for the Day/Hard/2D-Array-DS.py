import math


def hourglass(arr):
    max_num = -math.inf
    for x in range(4):
        for y in range(4):
            sm = arr[x][y] + arr[x][y+1] + arr[x][y+2] + arr[x+1][y+1] + arr[x+2][y] + arr[x+2][y+1] + arr[x+2][y+2]
            max_num = max((max_num, sm))
    print(max_num)

arr = [
        [1, 1, 1, 0, 0, 0], 
        [0, 1, 0, 0, 0, 0], 
        [1, 1, 1, 0, 0, 0], 
        [0, 0, 2, 4, 4, 0], 
        [0, 0, 0, 2, 0, 0], 
        [0, 0, 1, 2, 4, 0]]
hourglass(arr)