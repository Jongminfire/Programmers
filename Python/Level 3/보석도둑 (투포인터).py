from collections import defaultdict


def solution(gems):
    kinds = set(gems)   # 보석의 종류
    answer = [1, len(gems)]
    start, end = 0, 0
    dic = defaultdict(int)

    while end < len(gems):
        # 보석의 종류만큼 dic이 채워지지 않은 경우 end를 늘림
        if len(dic) < len(kinds):
            dic[gems[end]] += 1
            end += 1

        # 보석의 종류를 전부 못 담을 때 까지 start를 늘림
        while len(dic) == len(kinds) and start < end:
            # gems[start]가 1개일 경우 없앰
            if dic[gems[start]] == 1:
                del dic[gems[start]]
            # 1개 이상일 경우 1 감소
            else:
                dic[gems[start]] -= 1

            start += 1

            # 최소 거리일 때 갱신
            if end - start < answer[1]-answer[0]:
                answer = [start, end]

    return answer
