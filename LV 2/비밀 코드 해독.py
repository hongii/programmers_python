from itertools import combinations
def solution(n, q, ans):
    answer = 0
    for x in combinations(range(1, n+1), 5):
        flag = True
        for i, nums in enumerate(q):
            common_elements = set(nums) & set(x)
            if len(common_elements) != ans[i]:
                flag = False
                break
        if flag:
            answer += 1
            
    return answer