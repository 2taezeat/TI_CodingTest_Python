n = int(input())
l1 = list(map(int,input().split()))

d = [0] * 100

d[0] = l1[0]
d[1] = max(l1[0], l1[1])

for i in range(2,n):
    d[i] = max(d[i-1], d[i-2] + l1[i])


print(d[n-1])