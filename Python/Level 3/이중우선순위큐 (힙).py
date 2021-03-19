import heapq

def solution(operations):
    minq = []       # 최소 힙
    maxq = []       # 최대 힙

    for i in operations:
        a,b = i.split()
        
        if a == "I":
            heapq.heappush(minq,int(b))
            heapq.heappush(maxq,-int(b))

        else:
            if not minq:        # 큐 비어있을 경우 무시
                continue
            
            if b == "-1":
                value = heapq.heappop(minq)
                maxq.remove(-value)
            else:
                value = heapq.heappop(maxq)
                minq.remove(-value)
                
    if minq:
        return [-maxq[0],minq[0]]
    else:
        return [0,0]
    