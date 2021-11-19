from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for comb in list(permutations(dungeons,len(dungeons))):
        value = k
        cnt = 0
        
        for dun in comb:
            if dun[0] <= value:
                value -= dun[1]
                cnt += 1
        
        answer = max(cnt,answer)
    
    return answer if answer > 0 else -1