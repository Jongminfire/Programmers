from itertools import combinations


def solution(relation):
    cnt = 0

    # 키의 조합을 만들 배열
    keys = [i for i in range(len(relation[0]))]

    # 최소성을 위한 set
    candidate = set()

    for size in range(1, len(relation[0])+1):
        # combinations로 조합 만들기
        for comb in list(combinations(keys, size)):
            # 식별 검사를 위한 set
            s = set()
            check = True

            # 후보키 목록
            for c in candidate:
                # 집합으로 만들어서 차집합일 경우 검사안함
                if not {i for i in c} - {j for j in comb}:
                    check = False
                    break

            if check:
                for j in relation:
                    lst = []
                    for i in [num for num in comb]:
                        lst.append(j[i])

                    # set에는 list가 들어갈 수 없으므로 튜플 선언
                    item = tuple(v for v in lst)

                    if item not in s:
                        s.add(item)
                    else:
                        check = False
                        break

            # 조합으로 식별이 가능할 수 있으면 후보키에 추가 후 개수 늘리기
            if check:
                candidate.add(comb)
                cnt += 1

    return cnt
