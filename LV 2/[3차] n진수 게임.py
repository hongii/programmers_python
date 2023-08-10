# 2회차 코드
def convert(n, num):
    global numList
    convertNum = ""
    dic= {"10":"A", "11":"B", "12":"C", "13":"D", "14":"E", "15":"F"}
    while num > 0:
        num, mod = divmod(num, n)
        if mod >= 10:
            convertNum += dic[str(mod)]
        else:
            convertNum += str(mod)   
    numList.extend(list(convertNum[::-1]))
    
def solution(n, t, m, p):
    global numList
    i = p-1
    numList, res = ["0"], []
    for num in range(t*m):
        convert(n, num)
        while i < len(numList):
            res.append(numList[i])
            i += m
            if len(res) == t:
                return "".join(res)


# 1회차 코드
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