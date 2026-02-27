def solution(n, computers):
    visited = [False] * n

    def dfs(v):
        visited[v] = True
        for nxt in range(n):
            if computers[v][nxt] ==1 and not visited[nxt]:
                dfs(nxt)
                
    count = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            count += 1
            
    return count