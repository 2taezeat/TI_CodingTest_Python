import bisect
n = int(input())
l1 = list(map(int,input().split()))

def index1(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect.bisect_left(a, x)
    return (i < len(a) and a[i] == i)

a = -1
for i in range(n):
    x = l1[i]
    if x < 0:
        continue

    p = index1(l1,x)
    if p == True:
        a = x
        break

print(a)