v = int(input("Takeoff speed (km/hr): "))
s = int(input("distance (meters) over which the catapult accelerates the jet from rest to takeoff: "))

t = (2*s)/(v*1000/3600)
a = v/t

print(f"Acceleration: {a:.2f} m/s")