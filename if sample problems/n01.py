tot = input("Total: $")
conf = input("Are you a student? (y/n): ")
tot = float(tot)
print("------------------------------------------------------------------------------------")
print(f"Total purchase\t\t\t${tot}")

if conf == "y":
    print(f"Student's discount (20%)\t${(20/100)*tot:.2f}")
    tot = tot * (80/100)
    print(f"Discounted total\t\t${tot:.2f}")
    print(f"Sales tax (5%)\t\t\t${(5/100)*tot:.2f}")
    print(f"Total\t\t\t\t${(105/100)*tot:.2f}")
elif conf == "n":
    print(f"Sales tax (5%)\t\t\t${(5/100)*tot:.2f}")
    print(f"Total\t\t\t\t${(105/100)*tot:.2f}")