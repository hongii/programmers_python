def solution(answers):
    students = ["12345", "21232425", "3311224455"]
    correctCnt = []
    for i in range(3):
        cmpStr = students[i]
        if len(answers) > len(cmpStr):
            addSubStr = len(answers) - len(cmpStr)
            mulCnt = addSubStr // len(cmpStr)
            addCnt = addSubStr % len(cmpStr)
            cmpStr += cmpStr * mulCnt + cmpStr[:addCnt] 
        elif len(answers) < len(cmpStr):
            cmpStr = cmpStr[:len(answers)]
        print(cmpStr)
        
        cnt = 0
        for j in range(len(answers)):
            if str(answers[j]) == cmpStr[j]:
                cnt += 1
        correctCnt.append([cnt, i+1])      
    
    correctCnt.sort(reverse=True)
    res = [correctCnt[0][1]]
    for i in range(1, len(correctCnt)):
        if correctCnt[i][0] == correctCnt[0][0]:
            res.append(correctCnt[i][1])
        else:
            break
    
    return sorted(res)

''' 최적의 풀이
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
'''