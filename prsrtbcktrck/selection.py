lists = [9, 4, 5, 3, 0, 6, 2, 1, 8, 7]

for i in range(len(lists)):
    min = i
    for j in range(i+1, len(lists)):
        if lists[j] < lists[min]:
            min = j
    
    temp = lists[i]
    lists[i] = lists[min]
    lists[min] = temp
    
print(lists)