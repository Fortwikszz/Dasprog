N, C = input().split()
N, C = int(N), int(C)

if N % 3 == 0:
    if C == 1:
        print("Lili")
    if C == 2:
        print("Lala")
else:
    if C == 1:
        print("Lala")
    if C == 2:
        print("Lili")