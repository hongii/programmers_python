def solution(s):
    answer = False
    breakIdx = -1
    stack = []
    stack.append(s[0])
    for i in range(1, len(s)):
        if s[-1] == "(" or s[0] == ")":
            break
        if s[i] == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                breakIdx = i
                break
        else:
            stack.append(s[i])
            
    if not stack and breakIdx == -1: 
        answer = True
    return answer