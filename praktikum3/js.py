import sys
sys.setrecursionlimit(10 ** 9)

def path(i, j, peta, barang, m, n):
    #print(peta)
    
    if peta[i-1][j-1] == 0:
        peta[i-1][j-1] = "*"
    elif peta[i-1][j-1] == 2:
        peta[i-1][j-1] = "^"
        barang -= 1
    
    if i == n and j == m and barang == 0:
        return True
    
    if i < n:
        if (peta[i][j-1] == 0 or peta[i][j-1] == 2):
            if path(i+1, j, peta, barang, m, n):
                return True
    if j < m:
        if (peta[i-1][j] == 0 or peta[i-1][j] == 2):
            if path(i, j+1, peta, barang, m, n):
                return True
    if j > 1:
        if (peta[i-1][j-2] == 0 or peta[i-1][j-2] == 2):
            if path(i, j-1, peta, barang, m ,n):
                return True
    if i > 1:
        if (peta[i-2][j-1] == 0 or peta[i-2][j-1] == 2):
            if path(i-1, j, peta, barang, m, n):
                return True
    
    if peta[i-1][j-1] == "*":
        peta[i-1][j-1] = 0
    elif peta[i-1][j-1] == "^":
        peta[i-1][j-1] = 2
        barang += 1
    
    return False
        
m, n = map(int, input().split())
peta = [None]*n
barang = 0
for i in range(n):
    peta[i] = list(map(int, input().strip()))
    for j in range(m):
        if peta[i][j] == 2:
            barang += 1

path(1, 1, peta, barang, m, n)

for i in range(n):
    for j in range(m):
        if peta[i][j] == "^":
            peta[i][j] = "*"
        print(peta[i][j], end="")
    print()