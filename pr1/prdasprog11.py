import math

m = int(input("input m:"))
n = int(input("input n:"))

side1 = (abs(m**2 - n**2))
side2 = (2*m*n)
hypotenuse = (m**2 + n**2)

print(f"side1: {side1:.2f}")
print(f"side2: {side2:.2f}")
print(f"hypotenuse: {hypotenuse:.2f}")