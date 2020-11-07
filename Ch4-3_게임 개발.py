n, m = map(int,input().split())
x, y, d = map(int,input().split())
space = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for i in range(n):
    l = list(map(int,input().split()))
    space.append(l)

answer = 1

while(True):
    count = 0
    space[x][y] = space[x][y] + 1 
    for i in range(4):
        cd = d % 4

        if cd == 0:
            nx = x
            ny = y - 1
        elif cd == 1:
            nx = x + 1 
            ny = y 
        elif cd == 2:
            nx = x 
            ny = y + 1
        elif cd == 3:
            nx = x - 1 
            ny = y

        if space[nx][ny] == 0:
            space[nx][ny] = space[nx][ny] + 1
            x = nx
            y = ny
            answer = answer + 1
            d = d + 1
        else:
            count = count + 1
            d = d + 1

    if count == 4:
        if cd == 0:
            bx = x + 1
            by = y
        elif cd == 1:
            bx = x 
            by = y + 1 
        elif cd == 2:
            bx = x - 1 
            by = y
        elif cd == 3:
            bx = x
            by = y - 1

        if space[bx][by] != 0:
            break
        else:
            x = bx
            y = by


print(answer)