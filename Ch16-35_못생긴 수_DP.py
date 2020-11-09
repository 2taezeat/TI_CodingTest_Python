n = int(input())

d = [0] * n # 못생긴 수를 담기 위한 테이블
d[0] = 1
# 2배, 3배, 5배를 위한 인덱스
i2 = i3 = i5 = 0
# 처음에 곱셈값을 초기화
next2, next3, next5 = 2, 3, 5

# 1부터 n까지의 못생긴 수를 찾기
for k in range(1,n):
    # 가능한 곱셈 결과 중에서 가장 작은 수를 선택

    d[k] = min(next2,next3,next5)

    # 인덱스에 따라서 곱셈 결과를 증가
    if d[k] == next2:
        i2 = i2 + 1
        next2 = d[i2] * 2

    if d[k] == next3:
        i3 = i3 + 1
        next3 = d[i3] * 3

    if d[k] == next5:
        i5 = i5 + 1
        next5 = d[i5] * 5


print(d[n-1])