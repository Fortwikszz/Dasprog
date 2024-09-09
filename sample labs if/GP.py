n = input().split()

can = 1

for x in range(0,4):
    if n[0] < n[x]:
        can = 0
        break

if can == 1:
    print("YES HE CAN")
else:
    print("NO HE CAN'T")