def solution(n, times):
    # Min time: 1 min
    # Max time : Slowest Immigration officer doing all the job
    left, right = 1, max(times) * n
    answer = right
    
    while left <= right:
        mid = (left + right) //2
        
        # Total number of people that can be processed in mid time
        proc = 0
        for t in times:
            proc += mid // t
        
        # Can process more than n people => check if possible to reduce time
        if proc >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return answer