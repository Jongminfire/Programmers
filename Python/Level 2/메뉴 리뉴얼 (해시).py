from itertools import combinations


def solution(orders, course):
    answer = []

    # 코스별로 계산
    for c in course:
        dic = {}

        for o in orders:
            # order이 문자마다 다를 수 있으므로 sorted(o)로 조합 계산
            for comb in list(combinations(sorted(o), c)):
                item = ''.join(comb)

                if item in dic:
                    dic[item] += 1
                else:
                    dic[item] = 1

        # 가장 많은 메뉴 주문이 2회보다 작으면 무시
        if dic and max(dic.values()) < 2:
            continue
        # 가장 많이 주문된 메뉴 answer에 저장
        else:
            answer.append(list(k for k, v in dic.items()
                          if v == max(dic.values())))

    # 2차원 배열 1차원으로 합친 뒤 오름차순으로 정렬
    return sorted(sum(answer, []))
