n = int(input())

def func(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + func(n/2)
    elif n % 2 != 0:
        return 1 + func(n-1)
    
print(func(n))