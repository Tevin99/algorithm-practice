from collections import deque

def solution(board):
    n = len(board)
    INF = 10**9
    
    # 0:상 1:하 2:좌 3:우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    cost = [[[INF] * 4 for _ in range(n)] for _ in range(n)]
    q = deque()
    
    # 시작점: 아래 오른쪽만 이동 가능
    for d in (1,3):
        nx, ny = dx[d], dy[d]
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
            cost[nx][ny][d] = 100
            q.append((nx,ny,d,100))
            
    while q:
        x, y, d, c = q.popleft()
        
        # cost DP에는 업데이트 되었지만 큐에 
        # 더 비싼 비용이 남아있을 수 있어서
        if c != cost[x][y][d]:
            continue
        
        for nd in range(4):
            nx, ny = x + dx[nd], y + dy[nd]
            if not (0 <= nx < n and 0 <= ny <n):
                continue
            if board[nx][ny] == 1:
                continue
                
            nc = c + (100 if nd == d else 600)
            
            if nc < cost[nx][ny][nd]:
                cost[nx][ny][nd] = nc
                q.append((nx,ny,nd,nc))
                
    return min(cost[n-1][n-1])
    
        