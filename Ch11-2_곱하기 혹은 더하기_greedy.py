s = list(input())
sum1 = 0
a1 = int(s[0])
a2 = int(s[1])

if a1 == 0 or a1 == 1 or a2 == 0 or a2 == 1:
    sum1 = int(s[0]) + int(s[1])

else:
    sum1 = int(s[0]) * int(s[1])


for i in range(2,len(s)):
    b = int(s[i])
    if b == 0 or b == 1 or sum1 == 0 or sum1 == 1:
        sum1 = sum1 + b
    else:
        sum1 = sum1 * b

print(sum1)
