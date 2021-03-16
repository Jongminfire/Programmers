from math import gcd

def solution(arr):
    answer = 1

    # arr 차례대로 최소공배수 저장하며 구하기
    for i in range(len(arr)):
        answer = arr[i] * answer // gcd(arr[i],answer)

    return answer