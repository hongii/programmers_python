def solution(lottos, win_nums):
    correct_rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    zeroCnt = lottos.count(0)
    correctCnt = 0
    for x in lottos:
        if x in win_nums:
            correctCnt += 1
    return [correct_rank[correctCnt+zeroCnt], correct_rank[correctCnt]]