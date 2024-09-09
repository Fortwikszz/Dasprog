N = input()

sev = bool(False)

for i in range(0, len(N)):
    if N[i] == "4":
        sev = True

if sev:
    print("SEVER")
else:
    print("UNITE")