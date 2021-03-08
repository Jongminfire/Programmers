def solution(dirs):
    answer = 0
    board = []

    # 좌표의 변 배열로 선언
    for i in range(23):
        if i%2 == 0:
            board.append([False for i in range(10)])
        else:
            board.append([False for i in range(11)])
    
    # 현재 위치 x,y 좌표
    x = 5
    y = 5
    
    # 이동 처리
    for i in dirs:
        if i == "L":
            if x > 0:
                board[2*y][x-1] = True
                x -= 1
        elif i == "R":
            if x < 10:
                board[2*y][x] = True
                x += 1
        elif i == "U":
            if y > 0:
                board[2*y-1][x] = True
                y -= 1
        elif i == "D":
            if y < 10:
                board[2*y+1][x] = True
                y += 1

    # 방문 길이 계산
    for i in range(len(board)):
        answer += board[i].count(True)
    
    return answer