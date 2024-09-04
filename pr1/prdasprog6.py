grade = input("Enter desired grade =>")
minave = float(input("Enter minimum average required => "))
curave = float(input("Enter current avergae in course => "))
fincount = int(input("Enter how much the final counts as a percentage of the course grade => "))

need = (minave - ((100-fincount)/100) * curave) * (100/(fincount))

print(f"You need a score of {need:.2f} on the final to get a {grade}.")