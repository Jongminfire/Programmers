import heapq

def solution(scoville, K):
    answer = 0
    q = []
    
    for i in scoville:
        heapq.heappush(q,i)

    # K가 0인 경우 바로  0출력
    if K == 0:
        return 0
            
    # 제일 작은수가 0인 경우 지수를 증가 시킬 수 없으므로 -1 출력
    if q[0] == 0:
        return -1
    
    while q[0] < K :

        # heapq는 자식들의 정렬을 보장하지 않으므로 두번 나눠서 계산 해줌
        num = heapq.heappop(q)
        num += (heapq.heappop(q)*2)
        
        heapq.heappush(q,num)
        answer += 1
        
        # q가 2개 남은 경우 heappop에서 런타임에러 발생 할 수 있으므로 미리 계산
        if len(q) == 2:
            if q[0]+q[1]*2 < K:
                return -1
    
    return answer