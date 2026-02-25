# Greedy + Two Pointer
# Time Complexity: O(n log n)
# Space Complexity: O(1)

def solution(people, limit):
    people.sort()
    i, j = 0, len(people) - 1
    boats = 0

    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1      # 가벼운 사람도 같이 태움
        j -= 1          # 무거운 사람은 무조건 태워 보냄
        boats += 1

    return boats