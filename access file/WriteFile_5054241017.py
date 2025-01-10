file = open(r"D:\aaa\piton\dasprog\access file\MyName.txt", "w") 

for i in range(3): 
    name = input("Enter your name: ") 
    file.write(name) 
    file.write("\n") 
    
file.close() 

print("Data is written into the file.")

file1 = open(r"D:\aaa\piton\dasprog\access file\MyFamily.txt", "w") 
FamilyList = [] 
for i in range(4): 
    name = input("Enter the name of your family: ") 
    FamilyList.append(name + '\n') 
    
file1.writelines(FamilyList) 
file1.close() 
print("Data is written into the file.")