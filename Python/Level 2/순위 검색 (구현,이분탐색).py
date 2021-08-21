from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    answer = [0] * len(query)
    dic = defaultdict(list) # 초기 value 값은 리스트형식
    
    # info의 모든 경우의 수를 dic에 저장
    for information in info:
        lst = information.split(' ')
        key = lst[:-1]
        value = int(lst[-1])
        
        for i in range(0,5):
            # combinations로 0개부터 4개까지의 경우의 수를 배열 형태로 저장
            for v in combinations(key,i):
                temp = ''.join(v)
                dic[temp].append(value)
    
    # value로 저장된 배열 값 정렬
    for i in dic:
        dic[i].sort()

    # 쿼리와 저장 되어있는 dict 비교    
    for i,x in enumerate(query):
        q = x.split(' ')
        temp = q[:-1]
        value = int(q[-1])
        
        # 'and' 와 '-' 모두 제거
        while 'and' in temp:
            temp.remove('and')
            
        while '-' in temp:
            temp.remove('-')
            
        key = ''.join(temp)
        
        if key in dic:
            lst = dic[key]
            # value 값보다 작은 인덱스 위치 bisect_left 를 이용해 lower bound로 검색
            idx = bisect_left(lst,value)
            
            answer[i] = len(lst)-idx

    return answer