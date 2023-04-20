from collections import deque
def solution(s):
    dq = deque(s)
    cnt = 0
    check = 1 
    for i in range(len(s)):
        stack = []
        for j in range(len(s)):
            if stack and dq[j] == ")" and stack[-1] == "(":
                stack.pop()
            elif stack and dq[j] == "}" and stack[-1] == "{":
                stack.pop()
            elif stack and dq[j] == "]" and stack[-1] == "[":
                stack.pop()
            elif dq[j] == "(" or dq[j] == "{" or dq[j] == "[":
                stack.append(dq[j])
            else:
                check = 0
                break

        if check == 1 and not stack:
            cnt += 1
        check = 1
        dq.append(dq.popleft())

    return cnt
