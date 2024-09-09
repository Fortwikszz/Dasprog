M, N, T = input().split()
M, N, T = int(M), int(N), int(T)

pas = bool(False)
tot = M + N + 1

while T > 0:
    T -= 25
    if T > 0:
        while T > (T-60) and T > 0:
            T -= 5
            tot -= 1
            if tot == N:
                pas = True
                
if tot <= 0:
    tot = 0

if pas == True:
    print(f"YES! {tot}")
else:
    print(f"NO! {tot}")