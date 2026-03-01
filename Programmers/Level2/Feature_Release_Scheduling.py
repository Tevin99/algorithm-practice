from collections import deque

def solution(progresses, speeds):
    days = []
    for p, s in zip(progresses, speeds):
        remain = 100 - p
        days.append((remain + s - 1) // s)  # ceil
    
    q = deque(days)
    result = []
    
    current = q.popleft()
    count = 1
    
    while q:
        d = q.popleft()
        if d <= current:
            count += 1
        else:
            result.append(count)
            current = d
            count = 1
    
    result.append(count)  # 마지막 묶음
    return result
