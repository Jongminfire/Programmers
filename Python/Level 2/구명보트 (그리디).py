from collections import deque
# 시간초과 때문에 덱 사용

def solution(people, limit):
    cnt = 0
    people = deque(sorted(people))

    while len(people) != 0:
        index = 0
        now = people[-1]
        
        # 제일 큰수와 작은수의 합 비교
        while now < limit and index < len(people):
            now += people[index]
            index += 1
        
        # 제일 큰 수 제거
        people.pop()
        
        # list의 del로 없애면 시간초과 나기때문에 횟수만큼 popleft 해줌
        if now == limit:
            for _ in range(index):
                if len(people) != 0:
                    people.popleft()
        else:
            for _ in range(index-1):
                if len(people) != 0:
                    people.popleft()
            
        cnt += 1
    
    return cnt