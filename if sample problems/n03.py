def fun1():
    nyo = input("Enter 'T' for True or 'F' for False: ")
    if nyo == "T" or nyo == "t":
        return 1
    else:
        return 0

def fun2():
    print("fun2 executed")
    return 1

print("Testing 'and'")
if fun1() and fun2():
    print("Test of 'and' complete")
    
print("Testing 'or'")    
if fun1() or fun2():
    print("Test of 'or' complete")