yl = int(input("Yard length:"))
yw = int(input("Yard width:"))
hl = int(input("House length:"))
hw = int(input("House width:"))

Ysize = yl*yw
Hsize = hl*hw
time = (Ysize-Hsize)/2

print("Time requiered to cut the grass at the rate of 2 square feet/second is", time, "second")