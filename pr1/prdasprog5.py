vtbi = int(input("Volume to be infused => "))
mowi = int(input("Minutes over which to infuse => "))

rate = (60/mowi)*vtbi

print("VTBI:", vtbi, "ml")
print("RATE:", rate, "ml/hr")