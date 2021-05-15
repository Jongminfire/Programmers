def measure(num):
    cnt = 0
    for i in range(1, num+1):
        if num % i == 0:
            cnt += 1

    return True if cnt % 2 == 0 else False


def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if measure(i):
            answer += i
        else:
            answer -= i

    return answer
