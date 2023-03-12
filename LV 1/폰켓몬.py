def solution(nums):
    selectCnt = len(nums)//2
    if selectCnt > len(set(nums)):
        return len(set(nums))
    else:
        return selectCnt
        

''' 1차 시도: 테케 7번부터 시간초과
import itertools as it
def solution(nums):
    maxCnt = 0
    for cb in it.combinations(nums,len(nums)//2):
        if maxCnt < len(set(cb)):
            maxCnt = len(set(cb))
    return maxCnt
'''
