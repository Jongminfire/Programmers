from collections import deque,defaultdict

def solution(n, wires):
    answer = 101
    graph = defaultdict(list)
    
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    def bfs(start,remove,visit):
        dq = deque()
        dq.append(start)
        cnt = 0
        
        while dq:
            now = dq.popleft()
            visit[now] = True
            cnt += 1
            
            for node in graph[now]:
                if not visit[node] and [now,node] != remove:
                    dq.append(node)
        
        return cnt
    
    for w in wires:
        visit = [False for _ in range(n+1)]
        first = bfs(w[0],w,visit)
        second = bfs(w[1],w,visit)
        
        answer = min(abs(first-second),answer)
    
    return answer