import itertools as it
def solution(numbers):
    res = []
    for nums in it.combinations(numbers, 2):
        res.append(sum(nums))
    return sorted(set(res))