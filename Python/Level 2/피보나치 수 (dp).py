def solution(n):
    temp1 = 1
    temp2 = 1
    answer = 1
    
    if n == 1 or n == 2:
        return answer
    
    for i in range(n-2):
        answer = temp1 + temp2
        temp1 = temp2
        temp2 = answer
    
    return answer % 1234567