import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[prev] == target:
        return prev
    return -1

arr = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
target = 13
result = jump_search(sorted(arr), target)

print(result)