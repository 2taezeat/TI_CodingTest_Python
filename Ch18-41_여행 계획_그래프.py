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
########################################
n, m = map(int,input().split())
space = []
for i in range(n):
    space.append(list(map(int,input().split())))
plan = list(map(int,input().split()))
for p in range(len(plan)):
    plan[p] = plan[p] - 1

parent = [0] * (n)
for i in range(n):
    parent[i] = i

print(parent)

for i in range(0,n):
    space[i]
    l1 = []
    a = i
    for j in range(n):
        if space[i][j] == 1:
            l1.append((a,j))

    print(l1)

    for l in l1:
        a, b = l
        union_parent(parent,a,b)

print(parent)
result = True
for i in range(0,m-1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]):
        result = False

print(result)