n = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def odd(n,N):
    if N == -1:
        return 0
    elif n[N] % 2 == 0:
        return odd(n, N-1) + 0
    elif n[N] % 2 != 0:
        return odd(n, N-1) + 1
        
print(odd(n,N=len(n)-1))