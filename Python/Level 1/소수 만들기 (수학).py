import math
from itertools import combinations


def solution(nums):
    arr = [True for _ in range(3000)]
    answer = 0

    # 에라토스테네스의 체
    for i in range(2, int(math.sqrt(3000))+1):
        if arr[i] == True:
            j = 2
            while i * j < 3000:
                arr[i*j] = False
                j += 1

    for i in list(combinations(nums, 3)):
        total = sum(i)
        if total < 3000 and arr[total] == True:
            answer += 1

    return answer
