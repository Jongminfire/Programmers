def solution(n, build_frame):
    s = set()   # 요소 검사 빨리 하기 위해 set 활용
    answer = []

    def check(ans):
        for x, y, a in ans:
            # 기둥 설치
            if a == 0:
                # 바닥이거나 양 옆에 보가 있거나 아래 기둥이 있을 경우 설치 가능
                if y == 0 or (x - 1, y, 1) in ans or (x, y,1) in ans or (x, y - 1,0) in ans:
                    continue
                else:
                    return False
            # 보 설치
            elif a == 1:
                # 보 아래에 기둥이 있거나 양 옆에 두개의 보가 있을 경우 설치 가능
                if (x, y - 1, 0) in ans or (x + 1, y - 1, 0) in ans or ((x - 1, y, 1) in ans and (x + 1, y, 1) in ans):
                    continue
                else:
                    return False

        return True

    for x, y, a, b in build_frame:
        # 설치
        if b == 1:
            s.add((x, y, a))
            # s가 설치 불가능 한 경우 다시 삭제
            if not check(s):
                s.remove((x, y, a))

        # 삭제
        else:
            s.remove((x, y, a))
            # s가 삭제 불가능 한 경우 다시 추가
            if not check(s):
                s.add((x, y, a))

    for i in s:
        answer.append(i)

    # 요소 순서대로 정렬
    answer.sort(key=lambda x: (x[0], x[1], x[2]))
    return answer
