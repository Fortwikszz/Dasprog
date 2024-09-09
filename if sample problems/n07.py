m, d, y = input("Input date (month, day, year): ").split()

y = int(y)
d = int(d)
leap = bool(False)
if (y % 100 != 0 or y % 400 == 0) and y % 4 == 0:
    leap = True

match m:
    case m if m == "January" or m == "january" or m == "1":
        z = int(0)
    case m if m == "February" or m == "february" or m == "2":
        z = int(31)
    case m if m == "March" or m == "march" or m == "3":
        z = int(59)
        if leap == True:
            z = z + 1
    case m if m == "April" or m == "april" or m == "4":
        z = int(90)
        if leap == True:
            z = z + 1
    case m if m == "May" or m == "may" or m == "5":
        z = int(120)
        if leap == True:
            z = z + 1
    case m if m == "June" or m == "june" or m == "6":
        z = int(151)
        if leap == True:
            z = z + 1
    case m if m == "July" or m == "july" or m == "7":
        z = int(181)
        if leap == True:
            z = z + 1
    case m if m == "August" or m == "august" or m == "8":
        z = int(212)
        if leap == True:
            z = z + 1
    case m if m == "September" or m == "september" or m == "9":
        z = int(243)
        if leap == True:
            z = z + 1
    case m if m == "October" or m == "october" or m == "10":
        z = int(273)
        if leap == True:
            z = z + 1
    case m if m == "November" or m == "november" or m == "11":
        z = int(304)
        if leap == True:
            z = z + 1
    case m if m == "December" or m == "december" or m == "12":
        z = int(334)
        if leap == True:
            z = z + 1
        
print(f"Day number {z+d}")