print("TAXI FLARE CALCULATOR")
jalan = float(input("Enter beginning odometer reading=> "))
selesai = float(input("Enter ending odometer reading=> "))

distance = selesai - jalan
fare = distance * 1.50

distance = format(distance, ".2f")
fare = format(fare, ".2f")

print("You traveled a distance of ", distance, "miles. At $1.50 per mile, your fare is $", fare)