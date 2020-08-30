n, m, k = map(int,input().split())
l1 = list(map(int,input().split()))

l1.sort()
f = l1[-1]
s = l1[n-2]

c = (m // (k + 1)) * k
r = (m % (k + 1))

a = c + r

answer = a*f
answer = answer + (m - a) * s
print(answer)