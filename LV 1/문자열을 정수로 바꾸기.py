def solution(s):
    return -int(s[1:]) if s[0] == "-" else int(s) 

# 위의 코드 대신 return int(s) 로 바로 해줘도 통과... int()사용시, 굳이 양수와 음수를 따로 판별해서 출력할 필요 없음 