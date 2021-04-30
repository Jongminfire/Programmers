from collections import deque


def solution(m, n, board):
    q = deque()
    score = 0

    # board 행열 바꾸기
    for i in range(n):
        temp = deque()
        for j in range(m):
            temp.appendleft(board[j][i])
        q.append(temp)

    # board = list(map(list,zip(*board))) 로 바꿀 수 있음

    while True:
        # 삭제 저장할 리스트 (중복 값을 받기위해 set로 선언)
        remove = [set() for _ in range(len(q))]
        check = False   # 삭제할 값 없음을 검사하기 위한 변수

        for i in range(len(q)-1):
            for j in range(len(q[i])-1):
                if len(q[i+1]) <= j+1:
                    break

                if q[i][j] == q[i][j+1] == q[i+1][j] == q[i+1][j+1]:
                    remove[i].add(j)
                    remove[i].add(j+1)
                    remove[i+1].add(j)
                    remove[i+1].add(j+1)
                    check = True

        if not check:
            break

        # remove 좌표 만큼 점수 증가
        for i in remove:
            score += len(i)

        for i, v in enumerate(remove):
            v = deque(sorted(v))
            cnt = 0

            # 삭제한만큼 cnt를 증가시켜서 줄어드는 만큼 del 함
            while v:
                del q[i][v.popleft()-cnt]
                cnt += 1

    return score
