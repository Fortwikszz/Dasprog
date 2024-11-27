lists = [9, 4, 5, 3, 0, 6, 2, 1, 8, 7]

for i in range(len(lists)-1):
    for j in range(i, -1, -1):
        if lists[j] > lists[j+1]:
            temp = lists[j]
            lists[j] = lists[j+1]
            lists[j+1] = temp
        else:
            break
        print(lists)
        
print(lists)