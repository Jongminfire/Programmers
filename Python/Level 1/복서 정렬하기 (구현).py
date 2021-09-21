def solution(weights, head2head):
    info = []
    
    for i,v in enumerate(weights):
        info.append([v,i+1,0,0,0])
    
    for idx,v in enumerate(head2head):
        for i,j in enumerate(v):
            if j == 'W':
                info[idx][2] += 1
            
            if j == 'W' and weights[i] > weights[idx]:
                info[idx][3] += 1
            
            if j == 'L':
                info[idx][4] += 1
    
    # x[2]+x[4] 0인 경우 승률 0
    info.sort(key = lambda x:(x[2]/(x[2]+x[4]) if x[2]+x[4] > 0 else 0,x[3],x[0]),reverse=True)

    return [i[1] for i in info]