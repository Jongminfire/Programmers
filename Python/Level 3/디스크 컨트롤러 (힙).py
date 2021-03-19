import heapq

def solution(jobs):
    hq = []             # jobs순대로 힙큐에 저장
    rhq = []            # jobs순서 바꿔서 힙큐에 저장
    answer = []
    
    for i in jobs:
        heapq.heappush(hq,(i[0],i[1]))

    start = min(jobs)[0]
    
    while hq:
        while hq[0][0] <= start:
            heapq.heappush(rhq,(hq[0][1],hq[0][0]))
            heapq.heappop(hq)
            
            if not hq:
                break
        
        if rhq:
            e,s = heapq.heappop(rhq)
        
            start += e
            answer.append(start-s)
        
        else:
            start += 1
    
    # 남은 rhq 처리
    while rhq:
        e,s = heapq.heappop(rhq)
        
        start += e
        answer.append(start-s)
    
    return int(sum(answer)/len(answer))