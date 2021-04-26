from collections import defaultdict
from itertools import combinations


def solution(user_id, banned_id):
    banned = defaultdict(set)   # 밴 할 유저 저장할 dict
    cnt = defaultdict(int)      # 중복된 밴id 셀 dict

    for ban in banned_id:
        cnt[ban] += 1
        for u in user_id:
            if len(u) != len(ban):
                continue
            else:
                check = True
                # 밴 아이디와 일치하는지 검사
                for i in range(len(u)):
                    if ban[i] == '*':
                        continue
                    else:
                        if ban[i] != u[i]:
                            check = False
                            break

                if check:
                    banned[ban].add(u)

        # 밴 목록에 없으면 cnt dict에 값 없앰
        if not banned[ban]:
            cnt[ban] = 0

    check = set()

    # 밴 아이디 목록에 맞는 유저의 조합을 구함
    for ban in banned:
        # 밴 아이디의 유저와 중복된 만큼의 갯수로 조합을 구함
        item = list(combinations(banned[ban], cnt[ban]))
        if not check:
            for i in item:
                check.add(i)
        else:
            temp = set()
            for a in check:
                for i in item:
                    # set안에는 tuple만 가능하므로 tuple로 temp라는 list에 더할 값을 저장
                    temp.add(a + tuple(i))
            if temp:
                check = set()
                for i in temp:
                    check.add(tuple(sorted(i)))  # 순서가 다를 수 있으므로 정렬해서 추가

    ans = 0

    # 한 조합 안에 중복된 유저가 있을 수 있으므로 중복 검사
    for i in check:
        # 중복 검사를 위한 dict
        temp = defaultdict(int)

        for j in i:
            temp[j] += 1

        # 만약 모든 유저가 한번씩 나온 조합이라면 ans + 1
        if max(temp.values()) == 1:
            ans += 1

    return ans
