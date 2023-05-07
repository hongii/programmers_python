def convert(n, i):
    res = []
    dic = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
    
    if i == 0:
        return [0]
    
    while i > 0:
        num = i % n
        if i % n in dic.keys():
            num = dic[i%n]     
        res.append(str(num))
        i = i // n
        
    res.reverse() 
    return res
    
def solution(n, t, m, p):
    nums = []
    cnt = t * m
    i = 0
    while len(nums) < cnt:
        num = convert(n, i)
        i += 1
        nums.extend(num)
    
    res = ""
    for i in range(p-1, cnt, m):
        res += str(nums[i])
    return res