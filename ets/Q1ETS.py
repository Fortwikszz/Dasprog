q = int(input())

for _ in range(q):
    m = int(input())
    num = list(map(int, input().split()))
    count = [0]*10
    
    if m == 1:
        print("-1")
    else:
        for i in range(len(num)):
            for j in range(1,10):
                if num[i] == j:
                    count[j] += 1
                    
        Tinggiawal = 0
        Jumtinggi = 0
        Tinggi = 0
        
        for i in range(10):
            if count[i] > Tinggiawal:
                Tinggiawal = i
                Jumtinggi = 1
                Tinggi = count[i]
            elif count[i] == Tinggiawal:
                Jumtinggi += 1
        if Jumtinggi == 1:
            print(Tinggi,end="")
            print(f" * {Tinggiawal} = ",end="")
            print(Tinggi*Tinggiawal)
        else:
            print(Tinggiawal,end="")
            Total = Tinggiawal
            for j in range(10):
                if count[j] == Tinggi and j != Tinggiawal:
                    print(f"*{j}",end="")
                    Total *= j
            print(f" = {Total}")