def solution(arr1, arr2):
    res = []
    for i1 in range(len(arr1)):
        tmp = []
        for j2 in range(len(arr2[0])):
            num = 0
            for i2 in range(len(arr2)):
                num += arr1[i1][i2] * arr2[i2][j2]
            tmp.append(num)
        res.append(tmp)
    return res

'''
# comprehension과 zip을 활용한 풀이
def solution(arr1, arr2):
    return [[sum(a*b for a, b in zip(row1,col2)) for col2 in zip(*arr2)] for row1 in arr1]

# 해설  
zip(*arr2)를 이용한 unpacking 살펴보기(unzip)
=> for col2 in zip(*arr2) 에서, zip(*arr2)는 arr2의 이차원 배열에서 '열'의 요소들을 모아준다.
ex) arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]일 때,
    for col2 in zip(*arr2):
      print(col2)
    출력되는 col2값 순서 : [5, 2, 3]
                          [4, 4, 1]
                          [3, 1, 1]
'''