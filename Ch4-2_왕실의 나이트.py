space = [[0]*8 for i in range(8)] 
s = list(input())
x = s[0]
y = int(s[1])-1
if x == 'a':
    x = 0
elif x == 'b':
    x = 1
elif x == 'c':
    x = 2
elif x == 'd':
    x = 3
elif x == 'e':
    x = 4
elif x == 'f':
    x = 5
elif x == 'g':
    x = 6
elif x == 'h':
    x = 7

count = 0
dx = [2,2,-1,1,-2,-2,-1,1]
dy = [-1,1,2,2,1,-1,-2,-2]
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0<=nx<8 and 0<=ny<8:
        count = count + 1

print(count)