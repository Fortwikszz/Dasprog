x, y = map(int, input().split())
a = [[0 for _ in range(y)]for _ in range(x)]
for i in range(x):
    temp = str(input())
    for j in range(y):
        #print(temp[j])
        a[i][j] = int(temp[j])
    # print(temp)
#print(a)

count = 0
for i in range(x):
    for j in range(y):
        if a[i][j] == 1:
            for p in range(-1,2):
                for q in range(-1,2):
                    if (i+p>=0) and (j+q>=0) and (i+p<x) and (j+q<y):
                        if a[i+p][j+q] != 1:
                            count+=1

print(count)