lists = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
target = 13

result = -1
for i in range(len(lists)):
    if lists[i] == target:
        result = i
        break
        
print(result)