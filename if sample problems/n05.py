use = input("Data usage(GBs): ")
use = float(use)
charges = 0

match use:
    case use if use < 0:
        print("Bad data: Data usage cannot be negative")
    case use if use == 0:
        print("Bad data: Data usage invalid")
    case use if use > 0 and use <= 1:
        print("Charges = $250")
    case use if use > 1 and use <= 2:
        print("Charges = $500")
    case use if use > 2 and use <= 5:
        print("Charges = $1000")
    case use if use > 5 and use <= 10:
        print("Charges = $1500")
    case use if use > 10:
        print("Charges = $2000")