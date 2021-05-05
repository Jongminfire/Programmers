from collections import defaultdict, deque


def solution(n, path, order):
    graph = defaultdict(set)
    visit = [False for _ in range(n)]
    rules = defaultdict(int)    # order를 저장할 dict
    wait = defaultdict(int)     # order에 저장한 원소를 먼저 방문할 경우 저장할 dict

    dq = deque()
    dq.append(0)

    for a, b in order:
        rules[b] = a

        # 시작점은 0이므로 b가 0이면 무조건 False
        if b == 0:
            return False

    for a, b in path:
        graph[a].add(b)
        graph[b].add(a)

    while dq:
        num = dq.popleft()
        visit[num] = True

        for i in graph[num]:
            # a보다 b를 먼저 방문해야 할 때 b를 방문하지 않고 a를 방문한 경우 wait에 값 넣어줌
            if i in rules and not visit[rules[i]]:
                wait[rules[i]] = i
                continue

            if visit[i] == False:
                dq.append(i)

        # num이 wait에 있을 경우 wait도 덱에 넣음
        if num in wait:
            dq.append(wait[num])

    return False if False in visit else True
