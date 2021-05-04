from collections import deque


def solution(board):
    INF = int(1e9)
    visit = [[INF for _ in range(len(board))] for _ in range(len(board[0]))]
    visit[0][0] = 0

    def dfs(x, y, board, visit, direct):
        move = deque([(0, -1), (-1, 0), (0, 1), (1, 0)])

        # 코너의 경우를 먼저 계산하기 위해 같은 방향을 맨 뒤에 검사함. (이렇게 처리하지 않을 경우 테스트케이스에 잡히지 않는 오답있음)
        if direct != (0, 0):
            move.remove(direct)
            move.append(direct)

        for dx, dy in move:
            mx = x+dx
            my = y+dy

            if mx < 0 or mx >= len(board[0]) or my < 0 or my >= len(board):
                continue

            if board[mx][my] == 0:
                if direct == (0, 0) or direct == (dx, dy):
                    temp = visit[x][y] + 100
                else:
                    temp = visit[x][y] + 600

                if visit[mx][my] >= temp:
                    visit[mx][my] = temp

                    dfs(mx, my, board, visit, (dx, dy))

    dfs(0, 0, board, visit, (0, 0))

    return visit[-1][-1]
