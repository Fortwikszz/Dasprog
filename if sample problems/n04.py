name = input("Color: ")
if name[0] == "O" or name[0] == "o":
    print("ammonia")
elif name[0] == "B" or name[0] == "b":
    print("carbon monoxide")
elif name[0] == "Y" or name[0] == "y":
    print("hydrogen")
elif name[0] == "G" or name[0] == "g":
    print("oxygen")
else:
    print("Contents unknown")