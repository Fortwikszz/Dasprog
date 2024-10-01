n, k = map(int, input().split())
A = input().split()
beli = 0

for i in range(n):
    if int(A[i]) <= k:
     beli += 1
        
print(beli)