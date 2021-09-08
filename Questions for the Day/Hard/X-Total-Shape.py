'''
X Total Shapes 
Medium Accuracy: 65.93% Submissions: 8741 Points: 4
Given  a grid of n*m consisting of O's and X's. The task is to find the number of 'X' total shapes.
Note: 'X' shape consists of one or more adjacent X's (diagonals not included).
 

Example 1:

Input: grid = {{X,O,X},{O,X,O},{X,X,X}}
Output: 3
Explanation: 
The grid is-
X O X
O X O
X X X
So, X with same colour are adjacent to each 
other vertically for horizontally (diagonals 
not included). So, there are 3 different groups 
in the given grid.

Example 2:

Input: grid = {{X,X},{X,X}}
Output: 1
Expanation: 
The grid is- 
X X
X X
So, X with same colour are adjacent to each
other vertically for horizontally (diagonals
not included). So, there is only 1 group
in the given grid.
 

Your Task:
You don't need to read or print anything. Your task is to complete the function xShape() 
which takes grid as input parameter and returns the count of total X shapes.
 

Expected Time Compelxity: O(n*m)
Expected Space Compelxity: O(n*m)
 

Constraints:
1 ≤ n, m ≤ 100
'''

class Solution:
    def xShape(self, grid):
        normal=len(grid)
        max_stage=len(grid[0])
        check=[[False for j in range(max_stage)] for i in range(normal)]
        destination=[[0,1],[0,-1],[1,0],[-1,0]]
        rlst=0
        for i in range(0,normal) :
            for j in range(0,max_stage) :
                if grid[i][j]=='X' and check[i][j]==False :
                    rlst+=1
                    check[i][j]=True
                    random_num=[[i,j]]
                    while(len(random_num)>0) :
                        quick_fold=random_num[0]
                        random_num.pop(0)
                        for k in range(0,4) :
                            x_axis=quick_fold[0]+destination[k][0]
                            y_axis=quick_fold[1]+destination[k][1]
                            if x_axis>=0 and x_axis<normal and y_axis>=0 and y_axis<max_stage and grid[x_axis][y_axis]=='X' and check[x_axis][y_axis]==False:
                                check[x_axis][y_axis]=True
                                random_num.append([x_axis,y_axis])          
        return rlst


if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        normal, max_stage = map(int, input().split())
        grid = [['#' for i in range(max_stage)] for j in range(normal)]
        for i in range(normal):
            s = input().strip()
            for j in range(max_stage):
                grid[i][j] = s[j]
        obj = Solution()
        result = obj.xShape(grid)
        print(result)
