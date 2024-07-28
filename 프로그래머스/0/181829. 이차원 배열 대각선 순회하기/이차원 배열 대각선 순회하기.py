def solution(board, k):    
    return sum([board[i][j] for i in range(len(board)) for j in range(len(board[i])) if i + j <= k])