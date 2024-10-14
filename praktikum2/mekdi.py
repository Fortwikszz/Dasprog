n = int(input())
b = input().split()
sum = 1

for i in range(n):
    for j in range(i+1, n):
        if (int(b[i]) ^ int(b[j])) != 1:
            sum *= (int(b[i]) ^ int(b[j]))
    if sum == 0:
        break
        
print(sum)