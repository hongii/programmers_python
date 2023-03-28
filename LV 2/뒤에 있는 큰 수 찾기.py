# 입력값이 최대 10^7개 이므로 이중 for문 사용하면 시간초과 발생. 

def solution(numbers):
    stack = [] # numbers의 idx가 들어갈 스택
    res = [-1]*len(numbers)
    for i in range(len(numbers)):
        # 현재 값(numbers[i])이 스택의 top에 해당하는 idx의 numbers값(numbers[idx])보다 큰 경우, 이 현재값이 numbers[idx]의 바로 다음 큰 수가 된다.
        while stack and numbers[i] > numbers[stack[-1]]: 
            idx = stack.pop() 
            res[idx] = numbers[i] # numbers[idx]의 바로 다음 큰 수는 numbers[idx]가 된다.
        stack.append(i) 
    return res