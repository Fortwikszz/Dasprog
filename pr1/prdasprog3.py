th = int(input("Hours: "))
tm = int(input("Minutes: "))
t = th + (tm/60)

T = (4*t**2/(t+2))-20
T=format(T, ".2f")

print("Temperature since power failure:", T, "∘C")