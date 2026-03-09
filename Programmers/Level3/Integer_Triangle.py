def solution(triangle):
		# SLICING: copying triangle
    dp = [row[:] for row in triangle]  

    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
		    # Case 1: Very Left
            if j == 0:  
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            # Case 2: Very Right
            elif j == i:  
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            # Case 3: Mid
            else:  
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

    return max(dp[-1]) # Largest number in the last row