a = input().split()
b = input()
c = input()
d, e, f = input().split()

t = [0, 0, 0, 0, 0, 0, 0]
for i in range(0, 7):
    a[i] = int(a[i])
    t[i] = int(a[i])
b = int(b)
c = int(c)
d, e, f = int(d), int(e), int(f)

for x in range(0, b):
    for i in range(0, 7):
        a[(i + c) % 7] = t[i]
    for i in range(0, 7):
        t[i] = a[i]
        
print(a[d], a[e], a[f])
