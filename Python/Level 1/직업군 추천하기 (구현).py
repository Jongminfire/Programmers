from collections import defaultdict

def solution(table, languages, preference):
    answer = []
    dic = defaultdict(list)
    score = defaultdict(int)
    maxScore = 0

    for t in table:
        lst = t.split(' ')
        dic[lst[0]] = lst[1:]

    for sort in dic.keys():
        for idx, l in enumerate(languages):
            for i, v in enumerate(dic[sort]):
                if v == l:
                    score[sort] += preference[idx] * (5 - i)

    for k, v in score.items():
        if maxScore < v:
            maxScore = v
            answer = [k]
        elif maxScore == v:
            answer.append(k)

    return sorted(answer)[0]