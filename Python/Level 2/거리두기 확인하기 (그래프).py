from collections import deque


def bfs(x, y, place, visit):
    dq = deque()
    dq.append((x, y, 0))

    while dq:
        x, y, dist = dq.popleft()
        visit[x][y] = True

        for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if nx < 0 or nx > 4 or ny < 0 or ny > 4:
                continue

            if place[nx][ny] != 'X' and visit[nx][ny] == False:
                if place[nx][ny] == 'O':
                    dq.append((nx, ny, dist+1))
                if place[nx][ny] == 'P':
                    if dist >= 2:
                        dq.append((nx, ny, 0))
                    else:
                        return False

    return True


def solution(places):
    answer = []

    for place in places:
        ans = 1
        visit = [[False for _ in range(5)] for _ in range(5)]

        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P' and visit[i][j] == False:
                    if not bfs(i, j, place, visit):
                        ans = 0
                        break

        answer.append(ans)

    return answer
