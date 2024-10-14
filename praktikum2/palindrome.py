tex = input()
pal = bool(True)

for i in range(len(tex)):
    if tex[i] != tex[-(i+1)]:
        pal = False
        
if pal:
    print("Palindrome King!")
else:
    print("Bukan King!")