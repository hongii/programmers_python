from collections import deque
def checkWord(cmp, word):
    cnt = 0
    for i in range(len(cmp)):
        if cmp[i] != word[i]:
            cnt += 1
    return True if cnt == 1 else False

def solution(begin, target, words):
    dq = deque()
    dq.append((begin, 0))
    resWord, resStep = "", 0
    checked = {key:False for key in words}
    while dq:
        now, step = dq.popleft()
        if now == target:
            resWord = now
            resStep = step
            break
        for word in words:
            if not checked[word] and checkWord(now, word):
                checked[word] = True
                dq.append((word, step+1))

    return step if resWord == target and resStep > 0 else 0