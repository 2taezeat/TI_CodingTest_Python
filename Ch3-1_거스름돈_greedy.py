n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인
list1 = [500,100,50,10]

for coin in list1:
    count = count + ( n // coin ) # 해당 화폐로 거슬로 줄 수 있는 동전의 개수 세기
    n = n % coin

print(count)