# You are given a list `nums` representing the types of Pokémon you have.
# The total number of Pokémon is N, and you are allowed to choose only N/2 of them.
#
# Goal:
# Select N/2 Pokémon such that the number of DIFFERENT types is maximized.
#
# Key idea:
# - Count how many unique Pokémon types exist.
# - You cannot pick more than N/2 Pokémon.
# - Therefore, the answer is the smaller value between:
#     1) number of unique types
#     2) N/2

def solution(nums):
    half = len(nums) // 2
    kinds = len(set(nums))
    return min(half, kinds)
