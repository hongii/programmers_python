def solution(x):
    numListSum = sum(map(int, list(str(x))))  
    if x % numListSum == 0:
        return True
    else:
        return False
    
# ↓ 초기 코드
# numListSum = sum(list(map(int, list(str(x)))))에서 map object는 이미 iterable하기 때문에 list함수를 사용하지 않고 바로 sum함수를 이용하여 구할 수 있다.
# 따라서, ↓ 수정한 코드
# numListSum = sum(map(int, list(str(x))))  