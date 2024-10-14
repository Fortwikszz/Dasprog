t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    q = int(input())
    res = a[0]
    
    if q == 1:
        for j in range(k):
            temres = sum(a[0:j+1])
            if temres > res:
                    res = temres
            for r in range(0, n-j-1):
                temres = temres + a[r+j+1] - a[r]
                if temres > res:
                    res = temres
    if q == 2:
        for j in range(k):
            temres = sum(a[0:j+1])
            if temres < res:
                    res = temres
            for r in range(0, n-j-1):
                temres = temres + a[r+j+1] - a[r]
                if temres < res:
                    res = temres
    
    print(res)