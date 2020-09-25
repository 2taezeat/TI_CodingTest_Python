import bisect

n, x = map(int,input().split())
l1 = list(map(int,input().split()))
l1.sort()

lower = bisect.bisect_left(l1,x)
upper = bisect.bisect_right(l1,x)

result = upper - lower
if result == 0:
    print(-1)
else:
    print(result)
