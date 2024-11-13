import sys
sys.setrecursionlimit(10 ** 9)

def pcg(n, save):
    if n > 4:
        if n not in save:
            save[n] = ((pcg(n-4, save) % ((10**9)+7)) + (pcg(n-3, save) % ((10**9)+7)) + (pcg(n-2, save) % ((10**9)+7))) % (10**9+7)
            return save[n]
        else:
            return save[n]
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    elif n == 3:
        return 1
    elif n == 4:
        return 2

n = int(input())
count = 0
save = dict()

a = pcg(n, save)
      
print(a)