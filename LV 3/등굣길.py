def solution(m, n, puddles):
    dp = [[1]*m for _ in range(n)]
    for site in puddles:
        dp[site[1]-1][site[0]-1] = 0

    # 물웅덩이가 맨 윗쪽에 존재하는 경우, 해당 웅덩이 위치부터 가장 뒤까지 전부 0으로 변경(도달할 수 없는 지역)
    if 0 in dp[0]:
        idx = dp[0].index(0)
        for j in range(idx, m):
            dp[0][j] = 0

    # 물웅덩이가 맨 왼쪽에 존재하는 경우, 해당 웅덩이 위치부터 가장 아래까지 전부 0으로 변경
    for i in range(n):
        if dp[i][0] == 0:
            for k in range(i, n):
                dp[k][0] = 0
            break

    for i in range(1, n):
        for j in range(1, m):
            if dp[i][j] and 0 <= i-1 < n and 0 <= j-1 < m :
                dp[i][j] = dp[i-1][j] + dp[i][j-1] 

    return dp[n-1][m-1] % 1000000007


'''
# 최단 경로 갯수 구하는 방법 -> 합의 법칙 이용하기 (풀이 참고 유튜브 영상 출처(메가스터디) : https://www.youtube.com/watch?v=DaskzsweFv0)

# find 함수와 index 함수의 차이점
1. find() 함수 -> 문자열에서만 사용 가능
찾는 문자가 없는 경우에 -1을 반환함
문자열을 찾을 수 있는 변수는 문자열만 사용이 가능하다.  
리스트, 튜플, 딕셔너리 자료형에서는 find 함수를 사용할 수 없다.(사용하게 되면 AttributeError 에러가 발생한다.)

2. index() 함수 -> 리스트, 문자열, 튜퓰에서 사용 가능
찾는 문자가 없는 경우에 ValueError 에러가 발생한다.
문자열, 리스트, 튜플 자료형에서 사용 가능하고 딕셔너리 자료형에는 사용할 수 없어 AttributeError 에러가 발생한다.
'''