hei = float(input("Enter the height of the dam (in meters): "))
fr = float(input("Enter the flow rate of water (in cubic meters per second): "))

gravity = 9.80  
efficiency = 0.90  
waterdensity = 1000  

power = (waterdensity * fr * gravity * hei * efficiency) / 1e6
    
print(f"The hydroelectric dam will produce approximately {power:.2f} megawatts of power.")