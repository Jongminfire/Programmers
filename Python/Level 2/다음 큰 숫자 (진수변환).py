def solution(n):
    num = n+1
    cnt = bin(n).count('1')
    
    while True:
        if bin(num).count('1') == cnt:
            break
        num += 1
        
    return num