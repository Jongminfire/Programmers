import heapq

INF = int(1e9)


def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    distance = [INF] * (N+1)

    # 무방향 그래프이므로 양방향으로 간선 추가
    for i in road:
        graph[i[0]].append((i[1], i[2]))
        graph[i[1]].append((i[0], i[2]))

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

    # K 이하인 개수 출력
    return len([d for d in distance if d <= K])
