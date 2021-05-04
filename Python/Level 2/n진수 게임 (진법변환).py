import string
from collections import deque

tmp = string.digits+string.ascii_uppercase  # 10-15부터 대문자 A-F이므로 uppercase


# num을 base진법으로 바꾸는 함수
def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


def solution(n, t, m, p):
    num = 0  # 현재 숫자 (10진법 기준)
    string = deque([0])  # 진법 변환 후 말해야 하는 답
    order = 0   # 말해야 하는 순서
    answer = ''  # 튜브가 말하는 문자열
    cnt = 0     # 튜브가 말한 숫자의 개수

    while cnt < t:
        if order == p-1:
            answer += str(string.popleft())
            cnt += 1
        else:
            string.popleft()

        # 진법 변환 후 말해야 하는 답이 비었을 경우 현재 숫자 1증가 후 string에 진법 변환한 값 입력
        if not string:
            num += 1
            string = deque(convert(num, n))

        order = (order+1) % m

    return answer
