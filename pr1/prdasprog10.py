x1, y1 = input("Titik 1: ").split()
x2, y2 = input("Titik 2: ").split()

x1, x2, y1, y2 = float(x1), float(x2), float(y1), float(y2)

xmid = (x1+x2)/2
ymid = (y1+y2)/2

m1 = (y2-y1)/(x2-x1)
m2 = -1/m1

print(f"y = {m2}x + {-(m2*xmid)+ymid}") if -(m2*xmid)+ymid >= 0 else print(f"y = {m2}x {-(m2*xmid)+ymid}")