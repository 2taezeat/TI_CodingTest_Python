import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int,input().split())
graph = [ [ ] for i in range(n+1)]
distance = [INF] *(n+1)

for i in range(m):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start) )
    distance[start]

    while q: # 큐가 비어있지 않다면
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[ i[0] ]:
                distance[ i[0] ] = cost
                heapq.heappush(q, (cost, i[0] ))

dijkstra(start)

