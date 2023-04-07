# Counter와 set을 이용한 풀이 -> set에 원소를 추가할때는 O(1), Counter에서 원소 삽입 및 제거, 탐색할때는 O(1) 
from collections import Counter
def solution(topping): 
    cnt = 0
    c = Counter(topping) # O(n)
    cake1 = set()
    for i in range(len(topping)): # 반복문: O(n)
        cake1.add(topping[i]) # O(1)
        c[topping[i]] -= 1 # 탐색: O(1)

        if c[topping[i]] == 0:
            c.pop(topping[i]) # 제거: O(1)

        if len(cake1) == len(c):
            cnt += 1
    return cnt


''' 시간초과 -> set을 생성할 때는 시간 복잡도가 O(len(n))이므로, 
                아래의 코드에서 최악의 경우, 이중for문과 동일한 시간복잡도가 나온다. 
                따라서 시간초과가 뜨는것!(여기서 topping의 갯수(n)는 최대 100만개 이하로 주어짐)
def solution(topping):
    cnt = 0
    for i in range(1, len(topping)):
        cake1 = set(topping[:i])
        cake2 = set(topping[i:])
        if len(cake1) == len(cake2):
            cnt += 1
    return cnt
'''