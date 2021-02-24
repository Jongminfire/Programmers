visit = [False] * 201

def dfs(start,computers):
    visit[start] = True
    
    for i in range(len(computers)):
        if visit[i] == False and computers[start][i] == 1:
            dfs(i,computers)
    
    return start

def solution(n, computers):
    answer = 0
    for i in range(n):
        if visit[i] == False:
            dfs(i,computers)
            answer += 1
    return answer