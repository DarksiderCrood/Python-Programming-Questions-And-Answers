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
        n=len(grid)
        m=len(grid[0])
        mark=[[False for j in range(m)] for i in range(n)]
        dr=[[0,1],[0,-1],[1,0],[-1,0]]
        ans=0
        for i in range(0,n) :
            for j in range(0,m) :
                if grid[i][j]=='X' and mark[i][j]==False :
                    ans+=1
                    mark[i][j]=True
                    q=[[i,j]]
                    while(len(q)>0) :
                        f=q[0]
                        q.pop(0)
                        #print(f[0]," ",f[1])
                        for k in range(0,4) :
                            x=f[0]+dr[k][0]
                            y=f[1]+dr[k][1]
                            if x>=0 and x<n and y>=0 and y<m and grid[x][y]=='X' and mark[x][y]==False :
                                mark[x][y]=True
                                q.append([x,y])          
        return ans


if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n, m = map(int, input().split())
        grid = [['#' for i in range(m)] for j in range(n)]
        for i in range(n):
            s = input().strip()
            for j in range(m):
                grid[i][j] = s[j]
        obj = Solution()
        ans = obj.xShape(grid)
        print(ans)
