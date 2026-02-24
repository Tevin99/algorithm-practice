from collections import deque

def solution(maps):
    n = len(maps)        # 행
    m = len(maps[0])     # 열

    dist = [[-1] * m for _ in range(n)]
    q = deque([(0, 0)])

    dist[0][0] = 1  # 시작 칸도 거리 1로 카운트 (문제 요구)

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

    return dist[n-1][m-1]
	