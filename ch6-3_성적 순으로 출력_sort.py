n = int(input())
l1 = []
for i in range(n):
    a = list(input().split())
    name = a[0]
    score = a[1]
    l1.append([name,score])

l1.sort( key= lambda x: x[1] )
print(l1)
