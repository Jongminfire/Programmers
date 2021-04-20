INF = int(1e9)


def solution(n, s, a, b, fares):
    graph = [[INF] * (n+1) for _ in range(n+1)]

    for i in fares:
        v1, v2, cost = i
        graph[v1][v2] = cost
        graph[v2][v1] = cost

    # 자기 자신으로 향하는 거리 0으로 초기화
    for i in range(1, n+1):
        graph[i][i] = 0

    # 플로이드 와샬
    for k in range(1, n+1):
        for v1 in range(1, n+1):
            for v2 in range(1, n+1):
                graph[v1][v2] = min(graph[v1][v2], graph[v1][k] + graph[k][v2])

    ans = INF

    for i in range(1, n+1):
        ans = min(ans, graph[s][i]+graph[i][a]+graph[i][b])

    return ans
