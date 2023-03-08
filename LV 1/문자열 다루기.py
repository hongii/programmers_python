def solution(s):
    if (len(s) == 4 or len(s) == 6) and s.isdecimal():
        return True
    else:
        return False