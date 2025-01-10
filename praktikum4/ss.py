def merge(arr, left, mid, right):
    #print(arr)
    n1 = mid - left + 1
    n2 = right - mid

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
            ans[0] += 1
        else:
            arr[k] = R[j]
            j += 1
            ans[1] += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
        ans[0] += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
        ans[1] += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)
        ans[2]+=1

def print_list(arr):
    for i in arr:
        print(i, end=" ")
    print()

n = int(input())
lists = list(map(int, input().split()))


ans = [0]*3

merge_sort(lists, 0, len(lists)-1)
# print_list(lists)

for i in range(3):
    print(ans[i])