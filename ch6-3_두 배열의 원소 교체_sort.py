a, k = map(int,input().split())
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))

l1.sort()
l2.sort(reverse=True)
print(l1)
print(l2)

for i in range(k):
    l1[i] = l2[i]

print(sum(l1))
