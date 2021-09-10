def solution(N, stages):
    answer = []
    
    for i in range(1,N+1):
        a = stages.count(i)
        b = len(list(filter(lambda x : x >= i ,stages)))
        if b==0:
            answer.append((0,i))
        else:
            answer.append((a/b,i))
    
    answer.sort(key=lambda x : (-x[0], x[1]))
    
    return [i[1] for i in answer]