n , m = map(int,input().split())
l1 = []
for i in range(n):
    l1.append(min(list(map(int,input().split()))))

print(max(l1))

