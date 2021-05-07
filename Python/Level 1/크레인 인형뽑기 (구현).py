from collections import deque


def solution(board, moves):
    new_board = list(map(deque, zip(*board)))   # 2차원 행열 뒤집기
    basket = []
    point = 0

    # 행열의 0제거
    for i in new_board:
        while 0 in i:
            i.remove(0)

    for m in moves:
        if new_board[m-1]:
            value = new_board[m-1].popleft()
        else:
            continue

        if basket and basket[-1] == value:
            basket.pop()
            point += 2
        else:
            basket.append(value)

    return point
