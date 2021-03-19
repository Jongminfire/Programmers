from collections import deque

# 단어 일치 검사
def check(a,b):
    wrong = 0
    
    for i in range(len(a)):
        if a[i] != b[i]:
            wrong += 1
    
    if wrong == 1:
        return True
    return False

def bfs(start,cnt,words):
    dq = deque()
    
    # 시작 할 수 있는 지점 검사
    for i in range(len(words)):
        if check(start,words[i]):
            dq.append((words[i],i))
            cnt[i] = 1
    
    while dq:
        now,index = dq.popleft()
        
        for i in range(len(cnt)):
            if cnt[i] == 0:
                if check(now,words[i]):
                    dq.append((words[i],i))
                    cnt[i] = cnt[index] + 1
    
    return cnt
    
def solution(begin, target, words):
    cnt = [0 for _ in range(len(words))]
    
    # target이 words에 없으면 바로 0 반환
    if target not in words:
        return 0

    return bfs(begin,cnt,words)[words.index(target)]