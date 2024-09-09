n = input()
n = int(n)

prime = bool(True)

if n <= 1:
    prime = 0
elif n == 2:
    prime = 1
elif n % 2 == 0:
    prime = 0
else:
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            prime = 0
        
if prime:
    print("IT IS A PRIME")
else:
    print("IT IS NOT A PRIME")