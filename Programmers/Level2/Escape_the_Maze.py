from collections import deque

def bfs(start, target, maps):
    n,m = len(maps), len(maps[0])
    sx, sy = start ### 이렇게 하는 거 중요 len(start),len(start[0]) 아님
    tx, ty = target
    
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    q = deque([(sx,sy)])
    
    count = [[-1]*m for _ in range(n)]
    count[sx][sy] = 0
    
    while q:
        x, y = q.popleft()
        if (x,y) == (tx,ty): ### x,y 좌표로 먼저 검사하는 거 중요
            return count[x][y]
        
        for dx,dy in dirs:
            nx, ny = x + dx, y+dy
            if 0 <= nx < n and 0<= ny < m:
                
                if maps[nx][ny] != 'X' and count[nx][ny] == -1:
                    count[nx][ny] = count[x][y] + 1
                    q.append((nx,ny))

            
    return -1
    
    
    
def solution(maps):
    n,m = len(maps),len(maps[0])
    S = L = E = None
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                S = (i,j)
            elif maps[i][j] == 'L':
                L =  (i,j)
            elif maps[i][j] == 'E':
                E = (i,j) 
            
    a = bfs(S,L, maps)
    if a == -1:
        return -1
    b = bfs(L,E,maps)
    if b == -1:
        return -1
    
    return a + b
            
    