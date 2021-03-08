def solution(land):
    dp = [[0,0,0,0] for _ in range(len(land))]
    
    for i in range(4):
        dp[0][i] = land[0][i]
        
    dp[1][0] = land[1][0] + max(dp[0][1],dp[0][2],dp[0][3])
    dp[1][1] = land[1][1] + max(dp[0][0],dp[0][2],dp[0][3])
    dp[1][2] = land[1][2] + max(dp[0][0],dp[0][1],dp[0][3])
    dp[1][3] = land[1][3] + max(dp[0][0],dp[0][1],dp[0][2])
        
    for i in range(2,len(land)):
        dp[i][0] = land[i][0] + max(dp[i-1][1],dp[i-1][2],dp[i-1][3])
        dp[i][1] = land[i][1] + max(dp[i-1][0],dp[i-1][2],dp[i-1][3])
        dp[i][2] = land[i][2] + max(dp[i-1][0],dp[i-1][1],dp[i-1][3])
        dp[i][3] = land[i][3] + max(dp[i-1][0],dp[i-1][1],dp[i-1][2])
        
    return max(dp[len(land)-1][0],dp[len(land)-1][1],dp[len(land)-1][2],dp[len(land)-1][3])