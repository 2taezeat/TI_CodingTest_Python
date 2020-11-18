n = int(input())
l1 = list(map(int,input().split()))
l1.sort()

result = 0
count = 1
for i in range(len(l1)):
    
    if count >= l1[i]:
        result = result + 1
        count = 1
        continue

    count = count + 1

print(result)