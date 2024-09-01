import math

stdnt = int(input("Number of students: "))

sect = (stdnt/30)
sect = math.floor(sect)
left = stdnt-(sect*30)

print("Student:", stdnt-left)
print("Section:", sect)
print("Leftover:", left)