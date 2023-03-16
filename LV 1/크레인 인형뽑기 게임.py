def solution(board, moves):
    cnt = 0
    stack = []
    n = len(board[0])
    for i in range(len(moves)):
        for x in range(n):
            y = moves[i] - 1
            if board[x][y] != 0:
                stack.append(board[x][y])
                board[x][y] = 0
                break
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            cnt += 2

    return cnt