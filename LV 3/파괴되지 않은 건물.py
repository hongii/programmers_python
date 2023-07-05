# 두번째 코드 -> 다른 사람 해설 참고, 누적합 문제
# 해설 참고 - https://tech.kakao.com/2022/01/14/2022-kakao-recruitment-round-1/
def solution(board, skill):
    def changeAccBoard(turn, r1, c1, r2, c2, degree):
        global accBoard
        # turn == 1: 적, turn == 2: 아군
        dic = {1: [-degree, degree, degree, -degree], 2:[degree, -degree, -degree, degree]}
        accBoard[r1][c1] += dic[turn][0]
        accBoard[r2+1][c1] += dic[turn][1]
        accBoard[r1][c2+1] += dic[turn][2]
        accBoard[r2+1][c2+1] += dic[turn][3]
        # print(accBoard)
        
    def accSum():
        # 왼쪽 -> 오른쪽 행 누적합 구하기
        for i in range(len(accBoard)):
            for j in range(1, len(accBoard[0])):
                accBoard[i][j] += accBoard[i][j-1] 
        # print(accBoard)
        
        # 위쪽 열 -> 아래쪽 열 누적합 구하기
        for i in range(len(accBoard[0])):
            for j in range(1, len(accBoard)):
                accBoard[j][i] += accBoard[j-1][i] 
        # print(accBoard)
        
    def sumBoards():
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] += accBoard[i][j]
        # print(board)
        
    global accBoard
    accBoard = [[0 for _ in range(len(board[0])+1)] for _ in range(len(board)+1)]
    
    # (r1, c1), (r2+1, c1), (r1, c2+1), (r2+1, c2+1) 네 꼭지점 변화주기
    for i in range(len(skill)):
        turn, r1, c1, r2, c2, degree = skill[i]
        changeAccBoard(turn, r1, c1, r2, c2, degree)
    
    accSum()
    sumBoards()
    
    cnt = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                cnt += 1
    return cnt



'''첫번째 코드 -> LV1 스러운 풀이ㅋㅋ, 정확성 모두 통과, but, 예상대로 효율성 모두 시간초과
def solution(board, skill):
    def playGame(turn, r1, c1, r2, c2, degree):
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if turn == 1: # 적
                    board[i][j] -= degree
                elif turn == 2:
                    board[i][j] += degree
        
    for i in range(len(skill)):
        turn, r1, c1, r2, c2, degree = skill[i]
        playGame(turn, r1, c1, r2, c2, degree)
    # print(board)
    
    cnt = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                cnt += 1
    return cnt
'''