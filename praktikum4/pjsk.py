lists = list(map(int, input().split()))

def a(x):
    if len(str(sum(map(int, str(x))))) == 1:
        return (sum(map(int, str(x))))
    else:
        return a(sum(map(int, str(x))))
    
def b(x):
    return (a(x), x)
    
lists.sort(key=b)

for i in range(len(lists)):
    print(lists[i], end=" ")