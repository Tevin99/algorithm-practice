import heapq

def solution(N, road, K):
    # Make a graph
    graph = [[] for _ in range(N+1)]
    
    for a,b,cost in road:
        graph[a].append((b,cost))
        graph[b].append((a,cost))
        
    # Initialize Shortest path array
    INF = float('inf')
    distance = [INF] * (N+1)
    distance[1] = 0
    
    # Priority Queue (distance so far, current node)
    heap = []
    heapq.heappush(heap, (0,1))
    
    # Dijkstra
    while heap:
        dist, now = heapq.heappop(heap)
        
        # Ignore if shorter distance exists
        if dist > distance[now]:
            continue
        
        for nxt_node, cost in graph[now]:
            new_dist = dist + cost
            
            if new_dist < distance[nxt_node]:
                distance[nxt_node] = new_dist
                heapq.heappush(heap, (new_dist, nxt_node))
    
    # Count the number of village <= K
    answer = 0
    for d in distance:
        if d <= K:
            answer += 1
            
    return answer