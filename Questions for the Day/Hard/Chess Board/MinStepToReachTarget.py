'''
Have the function Quickknight (str) read str which will be a string consisting of 
the location of a knight on a standard 8x8 chess board with no other pieces on the 
board and another space on the chess board. The structure of str will be the following: 
"(x y) (a b)" where (x y) represents the position of the knight with x and y ranging 
from 1 to 8 and (a b) represents some other space on the chess board with a and b also 
ranging from 1 to 8. Your program should determine the least amount of moves it would 
take the knight to go from its position to position (a b). For example if str is 
"(2 3)(7 5)" then your program should output 3 because that is the least amount of 
moves it would take for the knight to get from (2 3) to (7 5) on the chess board.

Examples:

    Input: "(1 1) (8 8)"
    Output: 6

    Input: "(2 2) (3 3)" 
    Output: 2
'''

# This code is from GeeksFrorGeeks and 
# This code is contributed by
# Kaustav kumar Chanda
# Ref: https://www.geeksforgeeks.org/minimum-steps-reach-target-knight/

# I am working on my own code
class cell:
    def __init__(self, x = 0, y = 0, dist = 0):
        self.x = x
        self.y = y
        self.dist = dist
         

def isInside(x, y, N):
    if (x >= 1 and x <= N and
        y >= 1 and y <= N):
        return True
    return False
     

def minStepToReachTarget(knightpos,targetpos, N):
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]
     
    queue = []
    queue.append(cell(knightpos[0], knightpos[1], 0))
    visited = [[False for i in range(N + 1)] for j in range(N + 1)]
    visited[knightpos[0]][knightpos[1]] = True
    while(len(queue) > 0): 
        t = queue[0]
        queue.pop(0)
        if(t.x == targetpos[0] and t.y == targetpos[1]):
            return t.dist
        for i in range(8):  
            x = t.x + dx[i]
            y = t.y + dy[i] 
            if(isInside(x, y, N) and not visited[x][y]):
                visited[x][y] = True
                queue.append(cell(x, y, t.dist + 1))
 
 
if __name__=='__main__':
    N = 30
    knightpos = [2, 2]
    targetpos = [3, 3]
    print(minStepToReachTarget(knightpos,targetpos, N))

