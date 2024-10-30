def apple(n,N):
    if n > N:
        return apple(n-N,N)
    elif n == N:
        return 0
    else:
        return n
    
print(apple(3010,43))