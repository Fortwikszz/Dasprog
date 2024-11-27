def binser(lists, tgt, l, r):
    if l < r:
        mid = (l+r)//2
        if lists[mid] == tgt:
            return mid
        elif lists[mid] < tgt:
            return binser(lists, tgt, mid+1, r)
        elif lists[mid] > tgt:
            return binser(lists, tgt, l, mid-1)
    else:
        return -1
        
lists = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
target = 13
result = binser(lists, target, 0, len(lists)-1)

print(result)