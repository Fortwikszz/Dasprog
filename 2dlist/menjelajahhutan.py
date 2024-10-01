r, c, N = input().split()
coor = [[]*int(r)]*int(c)

for i in range(int(c)):
    coor[i] = input().split()
    for j in range(int(r)):
        coor[i][j] = int(coor[i][j])

move = input()
ic, jc = 0, 0
gold = coor[0][0]
gelah = bool(False)

for i in range(len(move)):
    if move[i] == "R":
        jc += 1
        gold += 3
        gold += coor[ic][jc]
    elif move[i] == "L":
        jc -= 1
        gold -= 2
        gold += coor[ic][jc]
    elif move[i] == "U":
        ic += 1
        gold += 3
        gold += coor[ic][jc]
    elif move[i] == "D":
        ic -= 1
        gold -= 2
        gold += coor[ic][jc]
    
    if ic < 0 or jc < 0:
        gelah = True
        break
    
print(gold)
if gelah:
    print("gerakanmu salah bung!")