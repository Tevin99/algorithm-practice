def solution(number, k):
    stack = []
    
    # Run thru "ALL" the numbers 
    # If OLD is smaller than NEW,
    # Discard
    for n in number:
        while k > 0 and stack and stack[-1] < n:
            stack.pop()
            k-=1
        stack.append(n) # First number always stacked
        
    return ''.join(stack[:len(stack)-k]) # return the oldest to height K from stack
            