t = int(input())
for i in range(t):
    n, m = map(int,input().split())
    dp = [[0] * (m + 1) for _ in range(n + 2)]
    l1 = list(map(int,input().split()))
    sl = []
    answer = 0
    for i in range(0,n):
        j = m*i
        a = l1[j:j+m]
        sl.append(a)

    for i in range(n):
        for j in range(m):
            dp[i+1][j+1] = sl[i][j]

    for j in range(1,m+1):
        for i in range(1,n+1):
            dp[i][j] = max( dp[i][j-1], dp[i+1][j-1], dp[i-1][j-1] ) + dp[i][j]

    for j in range(1,m+1):
        for i in range(1,n+1):
            answer = max(answer, dp[i][j])

    print(answer)