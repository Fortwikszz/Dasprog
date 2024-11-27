n = 4
k = 2
res = []

def backtrack(k, com):
    if k == 0 :
        res.append(com)
        return
    
    start = com[-1] + 1 if com else 1
    
    for i in range(start, (n-k+2)):
        backtrack(k-1, com+[i])
        
backtrack(k, [])

print(res)