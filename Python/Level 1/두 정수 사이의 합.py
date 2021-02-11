def solution(a, b):
    if a > b:
        swap = a
        a = b
        b = swap

    answer = 0

    for i in range(a, b + 1):
        answer += i

    return answer