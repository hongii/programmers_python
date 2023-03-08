def solution(arr1, arr2):
    res = [[]*len(arr1[i]) for i in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            res[i].append(arr1[i][j] + arr2[i][j])
    return res