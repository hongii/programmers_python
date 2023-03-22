def solution(s):
    if len(s) % 2 == 1:
        return 0

    stack = []
    stack.append(s[0])
    for i in range(1, len(s)):
        if stack and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])

    return 0 if stack else 1 

# 아이디어 -> stack 이용하여 풀기