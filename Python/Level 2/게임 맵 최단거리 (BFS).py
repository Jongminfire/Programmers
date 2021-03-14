from collections import deque

move = [[1,0],[-1,0],[0,1],[0,-1]]

def bfs(sx,sy,maps,visit):
    dq = deque()
    dq.append((sx,sy))
    cnt = 1
    visit[sx][sy] = cnt
    
    while dq:
        x,y = dq.popleft()
        cnt = visit[x][y]+1

        for i in range(4):
            dx = x + move[i][0]
            dy = y + move[i][1]

            if dx < 0 or dx >= len(maps) or dy < 0 or dy >= len(maps[0]):
                continue
            
            if visit[dx][dy] == -1 and maps[dx][dy] == 1:
                dq.append((dx,dy))
                visit[dx][dy]= cnt

    return visit

def solution(maps):
    visit = [[-1] * (len(maps[0])) for _ in range(len(maps))]

    return bfs(0,0,maps,visit)[len(maps)-1][len(maps[0])-1]