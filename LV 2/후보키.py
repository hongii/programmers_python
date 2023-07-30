'''
ps. 문제 조건
=> 관계 데이터베이스에서 릴레이션(Relation)의 튜플(Tuple)을 유일하게 식별할 수 있는 속성(Attribute) 또는 속성의 집합 중, 다음 두 성질을 만족하는 것을 후보 키(Candidate Key)라고 한다.
  * 유일성(uniqueness) : 릴레이션에 있는 모든 튜플에 대해 유일하게 식별되어야 한다.
  * 최소성(minimality) : 유일성을 가진 키를 구성하는 속성(Attribute) 중 하나라도 제외하는 경우 유일성이 깨지는 것을 의미한다. 
  즉, 릴레이션의 모든 튜플을 유일하게 식별하는 데 꼭 필요한 속성들로만 구성되어야 한다.
'''

# 2회차 풀이_최소성 먼저 판단 후 유일성 판단 
from itertools import combinations
def solution(relation):
    end = len(relation[0])
    s_cb = set()
    for i in range(1, end+1):
        colIdxCb = list(combinations(range(0, end), i))
        for cb in colIdxCb:
            s = set()
            for info in relation:
                check = True
                tmp = []
                
                for sub in s_cb: # 해당 후보키 조합이 최소성을 만족하는지 판단
                    if set(sub).issubset(set(cb)):
                        check = False # 최소성 만족 안하는 경우
                        break
                        
                if check: # 최소성 만족하는 경우에만 후보키 조합을 판단
                    for col in cb: 
                        tmp.append(info[col])
                    s.add(tuple(tmp))
                    if len(s) == len(relation): # 유일성 판단
                        s_cb.add(cb) # 유일성과 최소성 모두 만족하는 후보키 조합
    return len(s_cb)    


# 1회차 풀이_유일성 판단 후 최소성 판단
from itertools import combinations
def solution(relation):
    res = set()
    for i in range(1, len(relation[0])+1):
        # 가능한 키 조합 만들기(idx 조합으로 생성)
        cb = list(combinations(range(len(relation[0])), i))

        for c in cb:
            tmp = set()
            # 관계형 데이터베이스에서 데이터 한줄씩(row) 뽑아옴
            for info in relation:
                l = []
                
                # 키 조합 idx를 하나씩 뽑아와서 이 idx에 해당하는 data를 리스트 l에 집어넣음
                for j in c:
                    l.append(info[j])
                tmp.add(tuple(l)) # tmp집합에 키조합으로 뽑아온 데이터 리스트를 집어넣음 (set의 특징: 중복된 데이터가 있다면 넣지 않는다)

            # 중복된 데이터가 없는 경우 -> 후보키 가능성 있음(유일성 판단)
            if len(tmp) == len(relation):
                if len(res) == 0:
                    res.add(c)

                # 유일성 만족하는 키 조합 중에서 후보키 조건을 만족하기 위한 최소성 판단
                for s in res:
                    if set(s).issubset(set(c)):
                        break
                else:
                    res.add(c)

    return len(res)
