def apple(n,N):
    if n > N:
        return apple(n-N,N)
    else:
        return n
    
print(apple(2310,24))