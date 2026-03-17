def solution(n, costs):
    # Sort edges by cost in ascending order
    costs.sort(key=lambda x: x[2])
    
    # Initialize parent array for Union-Find
    parent = [i for i in range(n)]
    
    def find(x):
        # Path compression: make tree flat
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(a, b):
        # Find root of each node
        a, b = find(a), find(b)
        
        # If roots are different, merge them (no cycle)
        if a != b:
            parent[b] = a
            return True
        return False
    
    answer, edges = 0, 0
    
    # Iterate edges from smallest cost
    for a, b, cost in costs:
        # Add edge if it does not create a cycle
        if union(a, b):
            answer += cost  # Add cost
            edges += 1
            
            # Stop when we have n-1 edges (MST complete)
            if edges == n - 1:
                break
                
    return answer