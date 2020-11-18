n , k = map(int,input().split())
result = 0
    

while True:
    
    target = (n//k) * k
    result = result + (n - target)
    n = target

    
    if n < k:
        break
    
    n = n //k
    result = result + 1

result = result + (n-1)
print(result)