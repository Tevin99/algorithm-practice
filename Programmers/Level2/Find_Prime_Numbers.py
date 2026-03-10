from itertools import permutations

def is_prime(n):
    # Check if a number is prime
    if n < 2:
        return False
    
    # Only check divisibility up to √n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    nums = set()
    
    # Generate all permutations from length 1 to len(numbers)
    for i in range(1, len(numbers) + 1):
        for p in permutations(numbers, i):
            # Convert tuple to integer and store in a set to remove duplicates
            nums.add(int(''.join(p)))
    
    count = 0
    
    # Count how many generated numbers are prime
    for n in nums:
        if is_prime(n):
            count += 1
            
    return count