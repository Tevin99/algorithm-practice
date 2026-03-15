from collections import deque

def solution(n, edge):
    # 1) Build an adjacency list for the graph
    # Nodes are numbered from 1 to n (index 0 is unused)
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)  # Since the graph is undirected, add both directions

    # 2) Prepare distance and visited arrays
    # distance[i]: number of edges in the shortest path from node 1 to node i
    distance = [0] * (n + 1)
    visited  = [False] * (n + 1)

    # 3) Start BFS from node 1
    queue = deque([1])
    visited[1] = True  # Mark the starting node as visited
    # distance[1] is already 0 by default

    while queue:
        now = queue.popleft()  # Remove the current node from the queue

        # Check all adjacent nodes of the current node
        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = True

                # Update distance (increase by 1 edge from the current node)
                distance[nxt] = distance[now] + 1

                # Add the node to the queue to continue BFS
                queue.append(nxt)

    # 4) Find the maximum distance from node 1
    max_dist = max(distance)

    # Count how many nodes have this maximum distance
    return distance.count(max_dist)