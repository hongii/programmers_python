'''
# re 라이브러리 -> 정규식 표현을 이용하여 문자열 치환하기
=> re.sub(pattern, replace, text) : text 중 pattern에 해당하는 부분을 replace로 대체한다.
# (처음에 문제조건 잘못 이해해서 re라이브러리의 sub메서드를 사용하였는데 이후 조건 파악 다시하고 해당 코드는 삭제했음.)
# 삭제한 코드 :  str1 = re.sub('[^A-Za-z]', "", str1).lower(); str2 = re.sub('[^A-Za-z]', "", str2).lower(); 
'''
from collections import Counter
def solution(str1, str2):
    multiset1, multiset2 = [], []

    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha(): 
            multiset1.append(str1[i:i+2].lower())
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():    
            multiset2.append(str2[i:i+2].lower())

    c1, c2 = Counter(multiset1), Counter(multiset2)
    interCnt, unionCnt = 0, 0
    for v in (c1&c2).values():
        interCnt += v
    for v in (c1|c2).values():
        unionCnt += v
    J = 1 if len(multiset1) == 0 and len(multiset2) == 0 else interCnt / unionCnt

    return int(J * 65536)
