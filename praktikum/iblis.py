U = int(input())
K = int(input())
M = int(input())

M = int(M/2)
K = int(K/2)

U -= M*2
U -= K*5*5
U -= 1000

if U >= 0:
    print(f"Yey! Ucup Menang! HP tersisa: {U}")
else:
    print("Yah! Ucup Meninggoy.")