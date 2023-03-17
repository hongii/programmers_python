def solution(s, skip, index):
    answer = ""
    for i in range(len(s)):
        cnt = index
        j = 0
        while cnt > 0:
            j += 1 
            ch = chr((ord(s[i]) - ord("a") + j) % 26 + ord("a"))
            if ch not in list(skip):
                cnt -= 1
        ch = chr((ord(s[i]) - ord("a") + j) % 26 + ord("a"))
        answer += ch
        
    return answer

# 알파벳 mod연산 때문에 한참 뻘짓함...
