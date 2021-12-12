def solution(d, budget):
    current = 0
    cnt = 0
    
    for cost in sorted(d):
        current += cost
        if current > budget:
            return cnt
        cnt += 1
        
    return cnt