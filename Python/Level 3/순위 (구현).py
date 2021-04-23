from collections import defaultdict


def solution(n, results):
    # 승자와 패자 dict안의 set구조로 선언
    winner = defaultdict(set)
    loser = defaultdict(set)
    cnt = 0

    for i in results:
        winner[i[0]].add(i[1])
        loser[i[1]].add(i[0])

    for i in range(1, n+1):
        # 자신을 이긴 상대의 winner에 자신이 이긴 상대 추가
        for w in loser[i]:
            winner[w].update(winner[i])

        # 자신이 이긴 상대의 loser에 내가 진 상대 추가
        for l in winner[i]:
            loser[l].update(loser[i])

    for i in range(1, n+1):
        # 이긴 상대와 진 상대의 수 합이 n-1일 경우 순위를 알 수 있음
        if len(winner[i])+len(loser[i]) == n-1:
            cnt += 1

    return cnt
