def solution(triangle):
    # bottom-up으로 밑부터 검사
    for i in range(len(triangle)-1,0,-1):
        for j in range(len(triangle[i])-1):
            # 둘중 더 큰 값을 위에 더함
            triangle[i-1][j] += max(triangle[i][j],triangle[i][j+1])
    return triangle[0][0]