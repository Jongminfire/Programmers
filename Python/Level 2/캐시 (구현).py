from collections import deque

def solution(cacheSize, cities):
    cache = deque()     # deque(maxlen=cacheSize)로 선언하면 덱이 꽉 찼을 때 자동으로 첫번째 요소가 삭제됨
    answer = 0
    
    for i in cities:
        city = i.lower()
        
        if city not in cache:
            if cacheSize > 0:
                if len(cache) == cacheSize:
                    cache.popleft()
                cache.append(city)
            answer += 5
        else:
            cache.remove(city)
            cache.append(city)
            answer += 1
    
    return answer