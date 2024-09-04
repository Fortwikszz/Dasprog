age = input("Age: ")
sts = input("Status: ")
age = int(age)

if age > 59:
    if sts == "W":
        print("Working Senior")
    else:
        print("Retired Senior")
elif age > 20:
    print("Adult")
elif age > 12:
    "Teen"
else:
    print("Child")