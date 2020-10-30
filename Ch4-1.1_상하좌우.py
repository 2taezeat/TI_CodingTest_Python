n = int(input())
s = input().split()
x, y = 1,1

for str1 in s:
    if str1 == 'L':
        nx = x - 1
        ny = y
    elif str1 == 'R':
        nx = x + 1
        ny = y
    elif str1 == 'U':
        nx = x
        ny = y - 1 
    elif str1 == 'D':
        nx = x
        ny = y + 1

    if 0 < ny <= n and 0 < nx <= n:
        x = nx
        y = ny

print(x,y)