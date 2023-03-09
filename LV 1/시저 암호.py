def solution(s, n):
    res = ""
    for i in range(len(s)):
        num = ord(s[i]) + n 
        if " " == s[i]:
            res += " "
        elif ord('A') <= ord(s[i]) <= ord('Z'):
            if num > ord('Z'):
                res +=  chr(ord('A') + (num - ord('Z')) -1)
            else:
                res += chr((ord(s[i]) + n))
        elif ord('a') <= ord(s[i]) <= ord('z'):
            if num > ord('z'):
                res +=  chr(ord('a') + (num - ord('z')) -1)
            else:
                res += chr((ord(s[i]) + n))
    return res

''' 최적의 코드
def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n) % 26 + ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n) % 26 + ord('a'))

    return "".join(s)
'''