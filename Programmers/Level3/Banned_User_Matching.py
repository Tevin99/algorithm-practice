def solution(user_id, banned_id):
    # Create a list of candidate users for each banned_id pattern
    possible = []
    for b in banned_id:
        temp = []
        for u in user_id:
            # Skip if lengths are different (cannot match)
            if len(u) != len(b):
                continue
                
            match = True
            # Compare characters one by one
            for x, y in zip(u, b):
                # If banned pattern is not '*' and characters differ → not a match
                if y != '*' and x != y:
                    match = False
                    break

            # If the user_id matches the banned_id pattern, add it to candidates
            if match:
                temp.append(u)

        possible.append(temp)

    # Use a set to store unique combinations of matched users
    result = set()

    # DFS to explore all possible assignments
    def dfs(idx, path):
        # If we matched all banned_id patterns
        if idx == len(possible):
            # Sort the path so different orders count as the same combination
            result.add(tuple(sorted(path)))
            return

        # Try each candidate user for the current banned_id
        for user in possible[idx]:
            # Ensure the same user is not used more than once
            if user not in path:
                dfs(idx + 1, path + [user])
	
    # Start DFS from the first banned_id
    dfs(0, [])

    # Return the number of unique valid combinations
    return len(result)