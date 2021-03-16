def solution(s):
    cnt = [0,0]
    while s != "1":
        cnt[0] += 1
        cnt[1] += s.count('0')

        # s에서 0제거후 2진수 변환 뒤 0b 제거
        s = bin(len(s.replace('0',''))).replace('0b','')

    return cnt