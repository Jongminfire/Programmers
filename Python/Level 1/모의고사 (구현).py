def solution(answers):
    answer = []
    
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    
    f = 0
    s = 0
    t = 0
    
    for i in range(len(answers)):
        num = answers[i]
        
        if num == first[i%5]:
            f += 1
        if num == second[i%8]:
            s += 1
        if num == third[i%10]:
            t += 1
            
    value = max(f,s,t)
    
    if value == f:
        answer.append(1)
    if value == s:
        answer.append(2)
    if value == t:
        answer.append(3)
    
    return answer