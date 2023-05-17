def solution(board):
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j], board[i-1][j-1], board[i][j-1]) + 1

    maxSize = 0
    for i in range(len(board)):
        maxSize = max(maxSize, *board[i])
    return maxSize ** 2

'''
# dp를 이용한 풀이
=> 어느 한 점 (i,j)좌표에서, [왼쪽 대각선위, 위쪽, 왼쪽의 값] 중에 가장 작은값에 +1 해준 값을 board[i][j]에 넣어준다.
  board[i][j]에 갱신되는 값은 (i,j)점을 정사각형의 오른쪽 아래 꼭지점이라고 가정했을때의 정사각형 최대 길이 값이 저장된다.
  단, board[i][j]의 기존 값이 0인 경우는 pass하고 넘어간다.
  이제 board[i][j]에 갱신되는 각 요소는 자신(i,j)을 가장 오른쪽 아래에 두고 형성할 수 있는 정사각형의 최대 길이이므로,
  2차원 배열 안의 가장 큰 수를 구하여 정사각형의 크기는 한변의 제곱이므로 해당 값을 제곱하여 반환하면 된다.

  ex) '표시는 새로 갱신된 값(min(board[i-1][j], board[i-1][j-1], board[i][j-1]) + 1)을 표시한 것, *표시는 갱신 없이 pass한 표시
  0  1  1  1     0  1  1  1      0  1  1  1     0  1  1  1      0  1  1  1      0  1  1  1      0  1  1  1      0  1  1  1      0  1  1  1      0  1  1  1    
  1  1  1  1     1  1' 1  1      1  1  2' 1     1  1  2  2'     1  1  2  2      1  1  2  2      1  1  2  2      1  1  2  2      1  1  2  2      1  1  2  2      
  1  1  1  1     1  1  1  1      1  1  1  1     1  1  1  1      1  2' 1  1      1  2  2' 1      1  2  2  3'     1  2  2  3      1  2  2  3      1  2  2  3
  0  0  1  0     0  0  1  0      0  0  1  0     0  0  1  0      0  0  1  0      0  0  1  0      0  0  1  0      0  0* 1  0      0  0  1' 0      0  0  1  0*  
    step0           step1           step2          step3           step4           step5           step6           step7           step8           step9
  => 4*4 board에서는 (1, 1)~(3,3) 부분을 이중 for문을 통해 돌면서 정사각형 최대길이 값을 갱신한다.
    마지막 단계인 step9의 board에서 최대값인 3이 최대 정사각형 한변의 길이이므로 3*3 이 최대 정사각형 넓이가 된다.  
'''