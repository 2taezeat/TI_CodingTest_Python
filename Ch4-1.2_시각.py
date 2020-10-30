n = int(input())
l3 = [3,13,23,30,31,32,33,34,35,36,37,38,39,43,53]
answer = 0

for h in range(n+1):
    for m in range(0,60):
        for s in range(0,60):

            if s in l3 or m in l3 or h in l3:
                answer = answer + 1

print(answer)