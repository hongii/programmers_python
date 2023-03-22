def solution(brown, yellow):
    divisor = []
    # yellow의 약수 구하기
    for i in range(1, yellow+1):
        if yellow % i == 0:
            divisor.append(i)

    for num in divisor: 
        y = yellow // num # 동일한 가로길이를 가지는 여러줄의 세로줄로 연결하려면 yellow를 자신의 약수로 나눠야 한다. 
                          # ex) yellow가 15라면, 세로 4줄로 연결 불가능 -> 4는 15의 약수가 아님
        if (y+2)*2 + num*2 == brown: 
            return [y+2, num+2]
    '''
    두번째 for문 역할 해설
    ex) yellow=24, brown=24로 주어졌다면,
    1) yellow가 가로로 한 줄로(일렬로) 연결된 경우의 brown의 필요한 갯수를 계산 -> (24+2)*2 + 1*2 = 54 != 24(주어진 brown 갯수)
    2) yellow가 세로 두 줄로 연결된 경우의 brown의 필요한 갯수를 계산 -> (12+2)*2 + 2*2 = 32 != 24(주어진 brown 갯수)
    3) yellow가 세로 세 줄로 연결된 경우의 brown의 필요한 갯수를 계산 -> (8+2)*2 + 3*2 = 26 != 24(주어진 brown 갯수)
    4) yellow가 세로 네 줄로 연결된 경우의 brown의 필요한 갯수를 계산 -> (6+2)*2 + 4*2 = 2 == 24(주어진 brown 갯수)
      => 따라서, yellow가 세로 네줄로 연결된 카펫이 된다.
    '''