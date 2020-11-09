n, m = map(int,input().split())
coinlist = []
for i in range(n):
    coinlist.append(int(input()))

d = [99999] * (m+1)
d[0] = 0

for i in range(n):

    for j in range(coinlist[i], m + 1):

        d[j] = min(d[j], d[j-coinlist[i]] + 1)


if d[m] == 99999:
    print(-1)
else:
    print(d[m])