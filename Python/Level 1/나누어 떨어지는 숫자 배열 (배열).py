def solution(arr, divisor):
    answer = [i for i in arr if i % divisor == 0]
    return sorted(answer) if answer else [-1]