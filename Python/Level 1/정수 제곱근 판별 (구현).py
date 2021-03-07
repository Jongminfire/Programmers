import math

def solution(n):
    sqrt = math.sqrt(n)
    # python에서 **이 제곱을 뜻하므로 sqrt = n ** (1/2)으로도 가능하다
    return (sqrt+1) * (sqrt+1) if sqrt-round(sqrt) == 0 else -1