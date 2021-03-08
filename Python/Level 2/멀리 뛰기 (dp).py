def solution(n):   
    temp1 = 1
    temp2 = 2
    answer = 0
    
    if n == 1 or n == 2:
        return 1 if n==1 else 2
    
    for i in range(n-2):
        answer = temp1 + temp2
        temp1 = temp2
        temp2 = answer
        
    return answer % 1234567