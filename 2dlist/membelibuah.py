n, k = input().split()
A = input().split()
beli = 0
n = int(n)
k = int(k)

for i in range(n):
    if int(A[i]) <= k:
     beli += 1
        
print(beli)