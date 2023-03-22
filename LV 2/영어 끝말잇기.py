def solution(n, words):
    setWords = set()
    idx = 1
    lastCh = words[0][-1]
    setWords.add(words[0])
    for i in range(1, len(words)):
        if lastCh != words[i][0] or words[i] in setWords:
            return [(i+1) % n or n, idx]

        lastCh = words[i][-1]
        if words[i] not in setWords:
            setWords.add(words[i])

        if (i+1) % n == 0:
            idx += 1

    return [0, 0]