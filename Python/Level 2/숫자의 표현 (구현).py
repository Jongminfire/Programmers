def solution(n):
    cnt = 0
    for i in range(1,n+1):
        num = i
        
        while num < n:
            i += 1
            num += i
        
        if num == n:
            cnt += 1
        
    return cnt