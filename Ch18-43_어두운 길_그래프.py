def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int,input().split())
parent = [0] * n
for i in range(n):
    parent[i] = i

result = 0
edges = []
firstsum = 0
for i in range(m):
    a, b, c = map(int,input().split())
    firstsum = firstsum + c
    edges.append((c,a,b))

edges.sort()

for e in edges:
    c, a, b = e
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result = result + c

print(result)
print(firstsum - result)