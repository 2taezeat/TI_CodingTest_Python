# 그리디_2_이태경.py
n, m = map(int,input().split())
l1 = list(map(int,input().split()))

# 1부터 10까지의 공의 무게 count 
array = [0] * 11

for i in range(len(l1)):
    array[l1[i]] = array[l1[i]] + 1


result = 0
for i in range(1,m+1):
    n = n - array[i] # 무게가 i인 볼링공의 개수 제외

    result = result + (n * array[i]) # B가 선택하는 경우와 곱하기

print(result)