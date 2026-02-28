def solution(numbers, target):
    
    def dfs(idx, current):
        if idx == len(numbers):
            return 1 if target == current else 0
        
        return dfs(idx+1,current + numbers[idx]) + \
                dfs(idx+1,current - numbers[idx])
    
    return dfs(0,0)