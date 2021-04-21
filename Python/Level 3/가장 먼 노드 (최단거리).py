import heapq


def solution(n, edge):
    INF = int(1e9)
    graph = [[] for i in range(n+1)]

    distance = [INF] * (n+1)

    for v1, v2 in edge:
        graph[v1].append((v2, 1))
        graph[v2].append((v1, 1))

    # 다익스트라
    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0

        while q:
            dist, now = heapq.heappop(q)

            if distance[now] < dist:
                continue

            for i in graph[now]:
                cost = dist + i[1]

                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    dijkstra(1)

    # 가장 먼 정점 개수 세기
    return distance.count(max(distance[1:]))
