def solution(cards):
    res = []
    for i in range(len(cards)):
        # cards[i]가 0이 아니라면 아직 카드를 확인하지 않은 상자라는 뜻(cards[i]의 값은 다음번에 열어볼 상자의 번호가 저장되어 있음)
        if cards[i] != 0:
            idx = cards[i] - 1 # 다음번에 열어볼 상자번호의 idx값(ex. 3번 상자라면 idx는 2이다)
            cards[i] = 0 # 해당 상자를 개봉했다는 표시로 0을 넣어준다(같은 상자 두번다시 열지 않기 위함)
            cnt = 1

            # 개봉되지 않은 상자를 전부 열어본다(이미 열어본 상자가 나올때까지 반복문 수행)
            while cards[idx] != 0:
                cnt += 1
                tmp = cards[idx]
                cards[idx] = 0
                idx = tmp - 1                
            res.append(cnt)
    res.sort(reverse=True)

    return res[0] * res[1] if len(res) > 1 else 0

'''
상자를 개봉하여 카드를 확인한 상자에는 0으로 값을 넣어주어 다시 확인하지 않도록 한다.
'''
