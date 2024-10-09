n, m = map(int, input().split())
p = input().split(" ")
c = input().split(" ")

"""
for i in range(len(p)):
    for j in range(i+1, len(p)):
        if p[i] < p[j]:
            temp = p[i]
            p[i] = p[j]
            p[j] = temp
            
for i in range(len(c)):
    for j in range(i+1, len(c)):
        if c[i] > c[j]:
            temp = c[i]
            c[i] = c[j]
            c[j] = temp
"""

beli = 0
mines = 0
            
for i in range(n):
    if int(p[i]) > 0:
        beli += int(p[i])
    else:
        break

for i in range(m):
    if int(c[i]) < 0:
        mines += int(c[i])
    else:
        break
    
total = mines - beli

print(total)