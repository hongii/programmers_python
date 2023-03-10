def solution(n, arr1, arr2):
    board = [[0]*n for _ in range(n)] 
    res = []
    i = 0
    for x, y in zip(arr1, arr2):
        num1 = format(x, 'b').zfill(n)
        num2 = format(y, 'b').zfill(n)
        for j in range(n):
            if num1[j] == '0' and num2[j] == '0':
                board[i][j] = 0
            else:
                board[i][j] = 1
        i += 1
    # print(board)

    for i in range(n):
        resStr = ""
        for j in range(n):
            if board[i][j] == 1:
                resStr += "#"
            else:
                resStr += " "
        res.append(resStr)
    return res

''' 최적의 풀이
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0') # n자리의 공백에 "0"으로 채워넣는다.
        a12=a12.replace('1','#') # 문자열 "1"은 "#"으로 바꾼다.
        a12=a12.replace('0',' ') # 문자열 "0"은 " "(공백)으로 바꾼다.
        answer.append(a12)
    return answer

# 문자열 정렬하는 메소드
rjust
=> 오른쪽으로 정렬하도록 도와준다. rjust를 통해 공백의 수, 공백을 메워줄 문자를 넣어준다.

ljust
=> 왼쪽으로 정렬하도록 도와준다. ljust를 통해 공백의 수, 공백을 메워줄 문자를 넣어준다.

zfill
=> 0을 왼쪽(문자열 앞쪽)에 채워주는 역할을 한다.
'''