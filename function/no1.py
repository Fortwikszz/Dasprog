n = int(input())

def prime(n, N):
    if N == 0:
        return 1
    elif N != 1 and n % N == 0:
        return 0
    else:
        return prime(n, N-1)

if prime(n, int(n**(1/2))) == 1 and n != 1:
    print("prima")
else:
    print("not prima")