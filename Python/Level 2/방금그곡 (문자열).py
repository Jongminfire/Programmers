# 시간 분 단위로 변환
def time_car(time1, time2):
    t1 = list(map(int, time1.split(':')))
    t2 = list(map(int, time2.split(':')))

    return (t2[0]-t1[0]) * 60 + t2[1]-t1[1]


# 샾 붙은 문자열 처리 쉽도록 한 글자로 변환
def sharp_to_alpha(s):
    s = s.replace('C#', 'H')
    s = s.replace('D#', 'I')
    s = s.replace('F#', 'J')
    s = s.replace('G#', 'K')
    s = s.replace('A#', 'L')

    return s


def solution(m, musicinfos):
    answer = tuple()
    m = sharp_to_alpha(m)

    for music in musicinfos:
        music = music.split(',')
        t = time_car(music[0], music[1])
        name = music[2]
        sheet = sharp_to_alpha(music[3])

        if t < len(m):
            continue

        # 시간이 주어진 악보보다 긴 경우 악보를 반복해줌
        size = len(sheet)

        if t//size > 0:
            sheet = sheet * (t//size)
        sheet += sheet[:t % size]

        # t만큼 검사
        if m in sheet[:t]:
            if (answer and answer[1] < t) or not answer:
                answer = (name, t)

    return answer[0] if answer else '(None)'
