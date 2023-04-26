# 수정한 코드
def dfs(x, num, numbers, target):
    global res
    if x == len(numbers):
        if num == target:
            res += 1
            return
    else:
        dfs(x+1,num+numbers[x], numbers, target)
        dfs(x+1,num-numbers[x], numbers, target)
        
def solution(numbers, target):
    global res
    res = 0
    dfs(0, 0, numbers, target)
    
    return res

''' 첫번째 풀이 -> pass
def dfs(x, num, numbers, target):
    global res
    if x == len(numbers) - 1:
        if num == target:
            res += 1
            return
    else:
        dfs(x+1,num+numbers[x+1], numbers, target)
        dfs(x+1,num-numbers[x+1], numbers, target)
        
def solution(numbers, target):
    global res
    res = 0
    dfs(0, numbers[0], numbers, target)
    dfs(0, -numbers[0], numbers, target)
    
    return res
'''