def solution(word):
    answer = 0
    add = [781,156,31,6,1]
    alpha = ['A','E','I','O','U']
    
    for i,v in enumerate(word):
        answer += 1
        answer += alpha.index(v) * add[i]
    
    return answer