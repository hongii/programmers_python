def solution(numbers, hand):
    res = ""
    left, right = [3, 0], [3, 2]
    keyPadDic = {1:[0,0], 2:[0,1], 3:[0,2],
                 4:[1,0], 5:[1,1], 6:[1,2],
                 7:[2,0], 8:[2,1], 9:[2,2],
                          0:[3,1]}
    
    for i in range(len(numbers)):
        if numbers[i] in [1, 4, 7]:
            res += "L"
            left = keyPadDic[numbers[i]]
        elif numbers[i] in [3, 6, 9]:
            res += "R"
            right = keyPadDic[numbers[i]]
        else:
            leftDis = sum([abs(a-b) for a, b in zip(left, keyPadDic[numbers[i]])])
            rightDis = sum([abs(a-b) for a, b in zip(right, keyPadDic[numbers[i]])])
            if leftDis == rightDis:
                if hand == "left":
                    res += "L"
                    left = keyPadDic[numbers[i]]
                else:
                    res += "R"
                    right = keyPadDic[numbers[i]]
            elif leftDis < rightDis:
                res += "L"
                left = keyPadDic[numbers[i]]
            elif leftDis > rightDis:
                res += "R"
                right = keyPadDic[numbers[i]]
    return res