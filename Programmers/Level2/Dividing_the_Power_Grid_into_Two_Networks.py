from collections import defaultdict

def solution(n, wires):
    g = defaultdict(set)
    for a,b in wires:
        g[a].add(b)
        g[b].add(a)
        
    def dfs(start):
        visited = set()
        stack = [start]
        cnt = 0
        
        while stack:
            cur = stack.pop()
            if cur not in visited:
                visited.add(cur)
                cnt += 1
                stack.extend(g[cur])
        return cnt
                
    ans = n
    
    for a,b in wires:
        g[a].remove(b)
        g[b].remove(a)
        
        ans = min(ans,abs(n-2 * dfs(a)))
        
        g[a].add(b)
        g[b].add(a)
        
    return ans