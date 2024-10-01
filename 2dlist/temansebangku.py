N, r, c = map(int, input().split())

murid = [None]*N

for i in range(N):
    murid[i] = input().split(" ")

for i in range(N):
    adasebelah = bool(False)
    for j in range(N):
        if i != j:
            if murid[i][1] == murid[j][1]:
                if int(murid[i][2]) + 1 == int(murid[j][2]):
                    print(murid[j][0], end=" ")
                    adasebelah = True
                if int(murid[i][2]) - 1 == int(murid[j][2]):
                    print(murid[j][0], end=" ")
                    adasebelah = True
    if not adasebelah:
        print("0", end="")
    print()
                