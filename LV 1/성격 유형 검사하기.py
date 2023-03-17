def solution(survey, choices):
    answer = ""
    case = [("R","T"), ("C","F"), ("J","M"), ("A","N")]    
    testResult = {"R":0, "T":0, 
                  "C":0, "F":0,
                  "J":0, "M":0,
                  "A":0, "N":0}
    disagree_score = { 1:3, 2:2, 3:1 }
    agree_score = { 5:1, 6:2, 7:3 }
    
    for i in  range(len(choices)):
        if choices[i] in disagree_score.keys():
            testResult[survey[i][0]] += disagree_score[choices[i]]
        elif choices[i] in agree_score.keys():
            testResult[survey[i][1]] += agree_score[choices[i]]
    
    for key1, key2 in case:
        if testResult[key1] >= testResult[key2]:
            answer += key1
        else:
            answer += key2
    return answer