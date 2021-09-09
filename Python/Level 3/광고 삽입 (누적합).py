# 문자열 -> 초
def changeToSecond(time):
    h, m, s = map(int, time.split(':'))
    temp = h * 60 * 60
    temp += m * 60
    temp += s
    return temp


# 초 -> 문자열
def changeToString(time):
    time = int(time)
    h = str(time // 3600)
    m = str((time % 3600) // 60)
    s = str((time % 3600 % 60))

    if len(h) < 2:
        h = '0' + h

    if len(m) < 2:
        m = '0' + m

    if len(s) < 2:
        s = '0' + s

    return h + ':' + m + ':' + s


def solution(play_time, adv_time, logs):
    cnt = 0
    ans = 0
    play = changeToSecond(adv_time)
    total = changeToSecond(play_time)
    lst = [0] * (total + 1)

    for log in logs:
        start, end = log.split('-')
        start = changeToSecond(start)
        end = changeToSecond(end)

        # 누적합 구하기 위해 start에 +1 end에 -1
        lst[start] += 1
        lst[end] -= 1

    # lst[a]-lst[b]로 누적합의 합 구하기 위해 두번 더해줌
    for i in range(1, total + 1):
        lst[i] = lst[i] + lst[i - 1]

    for i in range(1, total + 1):
        lst[i] = lst[i] + lst[i - 1]

    # 초기 값은 0부터 play까지 재생
    cnt = lst[play]

    for i in range(total):
        # 총 길이를 넘는 경우 i부터 total까지 구해줌
        if i + play >= total:
            temp = lst[total] - lst[i]
        else:
            temp = lst[i + play] - lst[i]

        if temp > cnt:
            cnt = temp
            ans = i + 1

    return changeToString(ans)
