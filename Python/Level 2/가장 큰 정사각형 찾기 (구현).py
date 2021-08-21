def solution(board):
    ans = 0
    col = len(board)
    row = len(board[0])
    
    # 맨 앞줄은 고정
    dp = [[0]*(row+1) for _ in range(col+1)]
    
    # board 값이 1일 경우 dp의 최소값에 1 더해주기
    for i in range(1,col+1):
        for j in range(1,row+1):
            if board[i-1][j-1] == 1:
                dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                ans = max(ans,dp[i][j])

    return ans*ans