n = int(input())

print("+"+"-"*(2*n+1)+"+")

for i in range(n):
    print("| ", end="")
    for j in range(n):
        if (j+i)%2 == 0:
            print("V ", end="")
        else:
            print(". ", end="")
    print("|")
    
print("+"+"-"*(2*n+1)+"+")