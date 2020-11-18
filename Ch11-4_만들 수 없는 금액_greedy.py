n = int(input())
l1 = list(map(int,input().split()))
l1.sort()

sum1 = 0
target = 1
for i in range(len(l1)):

    print(l1[i],target)
    if l1[i] <= target:
        target = target + l1[i]
    else:
        break

print(target)