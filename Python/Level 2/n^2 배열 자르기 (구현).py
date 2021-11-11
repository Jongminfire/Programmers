def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        if (i+1)%n == 0:
            answer.append(n)
        else:
            temp = max((i+1)//n+1 ,(i+1)%n)
            answer.append(temp)
    
    return answer