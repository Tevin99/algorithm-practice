from collections import defaultdict

def solution(n, wires):
    # 각 노드별 연결고리 기록
    g = defaultdict(set)
    
    
    for a,b in wires:
        g[a].add(b)
        g[b].add(a)
        
    
    # DFS: 각 노드 연결노드 수 반환 
    def dfs(cur, visited):
        visited.add(cur)
        cnt = 1
        for nxt in g[cur]:
            if nxt not in visited:
                cnt += dfs(nxt,visited)
                
        return cnt
    
    ans = n
    
    # 간선 끊기
    for a, b in wires:
        g[a].remove(b)
        g[b].remove(a)
        
        visited = set()
        cnt = dfs(a,visited)
        
        ans = min(ans,abs(n- 2*cnt))
        
        g[a].add(b)
        g[b].add(a)
        
    return ans
    
    
    