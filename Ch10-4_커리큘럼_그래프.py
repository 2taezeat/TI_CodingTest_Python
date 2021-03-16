from collections import deque
import copy

v = int(input())
indegree = [0] * (v+1)

graph = [ [] for i in range(v+1) ]
time = [0] * (v+1)

for i in range(1,v+1):
    data = list( map(int,input().split() ))
    time[i] = data[0]

    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

print(graph)
print(indegree)
print(time)

result = copy.deepcopy(time)
q = deque()

for i in range(1,v+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
    for i in graph[now]:
        result[i] = max( result[i], result[now] + time[i] )
        indegree[i] -= 1

        # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
        if indegree[i] == 0:
            q.append(i)

for i in range(1, v+1):
    print(result[i])

