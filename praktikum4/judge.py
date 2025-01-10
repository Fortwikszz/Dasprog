m, n = map(int, input().split())

lists = []

def shit(x):
    if x >= 0:
        if lists[x] == lists[x-1]:
            return shit(x-1)
    
    return x
        
def shat(x):
    if x <= len(lists)-2:
        if lists[x] == lists[x+1]:
            return shat(x+1)
        
    return x

def binser(tgt, l, r):
    m = int((l+r)/2)
    
    if r-l == 1:
        if tgt == lists[m]:
            return shit(m)+1
        else:
            return m+1
    else:
        if tgt == lists[m]:
            return shit(m)
        elif tgt > lists[m]:
            return binser(tgt, m+1, r)
        elif tgt < lists[m]:
            return binser(tgt, l, m)

for i in range(n):
    templists = list(map(int, input().split()))
    lists += templists
    
#print(lists)

q = int(input())
r = list(map(int, input().split()))

tot = [0]*q
lists.sort()

for i in range(q):
    if r[i] > max(lists):
        tot[i] = len(lists)
    else:
        tot[i] = binser(r[i], 0, len(lists)-1)
        
for i in range(len(tot)):
    print(f"{tot[i]}", end=" ")