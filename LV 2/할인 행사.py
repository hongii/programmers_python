from collections import Counter
def solution(want, number, discount):
    dic = {}
    for i in range(len(want)):
        dic[want[i]] = number[i]

    first, last = 0, 9
    res = 0
    while last < len(discount):
        c = Counter(discount[first:last+1])
        first += 1
        last += 1
        if c == dic:
            res += 1
            
    return res
            
'''
from collections import Counter
def solution(want, number, discount):
    dic = {}
    for i in range(len(want)):
        dic[want[i]] = number[i]

    day = 0
    for i in range(len(discount)-10+1):
        c = Counter(discount[i:i+10])
        if c == dic:
            day += 1
        
    return day
'''