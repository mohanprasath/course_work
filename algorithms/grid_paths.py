# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Python3 program to Print all possible paths from  
# top left to bottom right of a mXn matrix 
allPaths = [] 
def findPaths(maze,m,n): 
    path = [0 for d in range(m+n-1)] 
    findPathsUtil(maze,m,n,0,0,path,0) 
      
def findPathsUtil(maze,m,n,i,j,path,indx): 
    global allPaths 
    # if we reach the bottom of maze, we can only move right 
    if i==m-1: 
        for k in range(j,n): 
            #path.append(maze[i][k]) 
            path[indx+k-j] = maze[i][k] 
        # if we hit this block, it means one path is completed.  
        # Add it to paths list and print 
        # print(path) 
        allPaths.append(path) 
        return 
    # if we reach to the right most corner, we can only move down 
    if j == n-1: 
        for k in range(i,m): 
            path[indx+k-i] = maze[k][j] 
          #path.append(maze[j][k]) 
        # if we hit this block, it means one path is completed.  
        # Add it to paths list and print 
        # print(path) 
        allPaths.append(path) 
        return 
      
    # add current element to the path list 
    #path.append(maze[i][j]) 
    path[indx] = maze[i][j] 
      
    # move down in y direction and call findPathsUtil recursively 
    findPathsUtil(maze, m, n, i+1, j, path, indx+1) 
      
    # move down in y direction and call findPathsUtil recursively 
    findPathsUtil(maze, m, n, i, j+1, path, indx+1)
    
def generateMatrix(n):
    if n<=0:
        return [] 

    matrix=[row[:] for row in [[0]*n]*n]
    
    row_st=0
    row_ed=n-1
    
    col_st=0
    col_ed=n-1
    current=1
    
    while (True):
        if current>n*n:
            break
        for c in range (col_st, col_ed+1):
            matrix[row_st][c]=current
            current+=1
        row_st+=1
        for r in range (row_st, row_ed+1):
            matrix[r][col_ed]=current
            current+=1
        col_ed-=1
        for c in range (col_ed, col_st-1, -1):
            matrix[row_ed][c]=current
            current+=1
        row_ed-=1
        for r in range (row_ed, row_st-1, -1):
            matrix[r][col_st]=current
            current+=1
        col_st+=1
    return matrix


if __name__ == '__main__':
    
    for i in range(2, 11):
        all_paths_count = 0
        maze=generateMatrix(i)
        # print(maze)
        for l in range(i):
            for m in range(i):
                # print(l, m)
                if (l!=0 and m!=0):
                    temp_count = findPaths(maze,l,m)
        print("i is ", i)
        print("all paths count is ", len(allPaths))
        # print(allPaths) 