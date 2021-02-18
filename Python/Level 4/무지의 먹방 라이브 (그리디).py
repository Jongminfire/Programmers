# 배열을 오름차순으로 유지하기 위해 heapq 사용
import heapq

def solution(food_times, k):
    # 모든 음식을 먹는 경우 -1 반환
    if sum(food_times) <= k :
        return -1
    
    q = []
    
    for i in range(len(food_times)):
        # (시간,번호)로 heapq에 입력
        heapq.heappush(q,(food_times[i],i+1))
        
    # 지난 시간을 저장하기 위한 변수
    sum_value = 0

    # 바로 이전 음식의 시간을 저장하기 위한 변수
    previous = 0

    # 남은 음식의 길이를 저장할 변수
    size = len(food_times)
    
    # 지난 시간 + 다음 음식을 다 먹게되는 시간이 k보다 작을 경우
    while sum_value + ((q[0][0] - previous) * size) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * size
        size -= 1
        previous = now

        # 남아있는 음식 중 제일 작은 시간을 가진 값을 더해주고 사이즈를 줄임
        
    # 남아있는 음식은 원래의 번호대로 오름차순 정렬
    result = sorted(q,key = lambda x: x[1])

    # 남은시간에서 k시간까지 계산했을 때 번호 출력
    return result[(k-sum_value) % size][1]
        