s = list(input())
sum1 = 0
r = []

for i in range(len(s)):
    try:
        sum1 = sum1 + int(s[i])
    except:
        r.append(s[i])

r.sort()
r.append(str(sum1))
r = ''.join(r)

print(r)