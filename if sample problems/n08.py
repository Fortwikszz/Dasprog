print("(1) First Free Service")
print("(2) Second Free Service")
num = input("Enter the number of free service>> ")
mil = input("Enter number of Miles>> ")

mil = int(mil)

if num == "1":
    if 1500 < mil <= 3000:
        print("Vehicle must be serviced")
    else:
        print("Vehicle must not be serviced")
elif num == "2":
    if 3001 < mil <= 4500:
        print("Vehicle must be serviced")
    else:
        print("Vehicle must not be serviced")
else:
    print("Error, please choose Service")