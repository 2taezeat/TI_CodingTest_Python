n = int(input())
l1 = []

for i in range(n):
    l1.append(int(input()))

l1.sort(reverse=True)

print(l1)