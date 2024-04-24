from heapq import *

n, m = map(int, input().split())
INF = int(1e9)
start = int(input())
graph = [[] for i in range(n)]
distance = [float('inf') for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(startNode):
    q = []
    heappush(q, (0, startNode))
    distance[startNode] = 0

    while q:  # 큐가 비어 있지 않다면
        curCost, node = heappop(q)

        if distance[node] < curCost:  # 만약 지금 꺼낸 것보다 더 짧은 경로를 알고 있다면 지금 꺼낸 것을 무시
            continue

        for nxt, weight in graph[node]:
            nCost = curCost + weight
            if nCost < distance[nxt]: # 더 짧은 경로를 발견하면, dist를 갱신하고 우선수위 큐에 넣는다.
                distance[nxt] = nCost
                heappush(q, (nCost, nxt))
