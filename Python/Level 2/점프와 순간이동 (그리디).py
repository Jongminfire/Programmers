def solution(n):
    ans = 0
    now = n
    
    while now != 0:
        if now % 2 == 0:
            now /= 2
        else:
            now -= 1
            ans += 1
    
    return ans