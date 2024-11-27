import time
lists = [9, 4, 5, 3, 0, 6, 2, 1, 8, 7]

def merge(lists, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = lists[l + i]
 
    for j in range(0, n2):
        R[j] = lists[m + 1 + j]

    i = 0
    j = 0
    k = l
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            lists[k] = L[i]
            i += 1
        else:
            lists[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        lists[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        lists[k] = R[j]
        j += 1
        k += 1
        
def ms(lists, l, r):
    if l < r:
        m = l+(r-l)//2
        ms(lists, l, m)
        ms(lists, m+1, r)
        merge(lists, l, m, r)

start = time.time()
ms(lists, 0, len(lists)-1)
end = time.time()

print(lists)
print(end-start)