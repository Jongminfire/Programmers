import string

tmp = '124'


# 진법변환 코드에서 tmp를 '124'로 둠
def convert(num, base):
    q, r = divmod(num-1, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


def solution(n):
    # n을 '124'를 사용한 3진법 수로 변환
    return convert(n, 3)
