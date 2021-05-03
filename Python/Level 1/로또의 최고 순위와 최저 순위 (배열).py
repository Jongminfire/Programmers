def solution(lottos, win_nums):
    answer = [7, 7]

    for w in win_nums:
        if w in lottos:
            answer[0] -= 1
            answer[1] -= 1

    answer[0] -= lottos.count(0)

    return [min(answer[0], 6), min(answer[1], 6)]
