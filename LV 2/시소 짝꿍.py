from collections import Counter
def solution(weights):
    cnt = 0
    dic = Counter(weights)
    for w in weights:
        dic[w] -= 1 # 자기자신 제외
        # 몸무게 w인 사람과 짝꿍을 이룰 수 있는 거리비 -> 1:1, 1:2(and 2:1), 2:3(and 3:2), 3:4(and 4:3)
        # 따라서, 짝꿍을 이룰 수 있는 몸무게는 -> w, w/2, 2w, (w*3)/2, (w*2)/3, (w*4)/3, (w*3)/4 이다.
        cnt += dic[w] + dic[w*2] + dic[w/2] + dic[(w*2)/3] + dic[(w*3)/2] + dic[(w*4)/3] + dic[(w*3)/4]
        dic[w] += 1 # 원래대로 포함시키기
    return cnt // 2 # 중복값 제외 -> ex) {180, 360}씽의 경우, cnt는 w = 180일때 cnt를 증가시키고, 이후 w = 360일때 똑같이 cnt를 증가시키므로 cnt//2를 해줘야 한다.

'''
# Counter 사용법 추가
1. Counter의 반환값 형태는 dict형태이다. -> dic.items(), dic.keys() 바로 사용 가능
2. Counter에 없는 key의 value값을 불러오는 경우, 0을 반환한다 !!!!!!!! -> KeyError발생 안함!!
'''