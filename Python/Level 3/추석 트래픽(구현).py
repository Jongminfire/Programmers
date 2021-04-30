from collections import defaultdict


def solution(lines):
    lst = []
    dic = defaultdict(int)
    answer = 0

    for i in lines:
        day, time, length = i.split(' ')
        hour, minute, second = time.split(':')
        length = length[:-1]
        end = (float(hour)*60*60 + float(minute) * 60 + float(second))*1000
        start = (end-float(length)*1000+1)

        for i in range(int(start), int(end)+1000):
            dic[i] += 1

    return max(dic.values())


"""
각 구간을 1000번씩 dic에 등록해서 가장 큰 values 값을 찾는 방법인데 효율성이 매우 안좋으니
슬라이딩 윈도우 방식으로 다시 풀어봐야 할듯
"""
