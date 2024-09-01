goil = int(input("Number of gallons oil: "))
effi = input("Efficiency: ")

#jika input menggunakan %, akan menghilangkan "%" menggunakan fungsi di bawah ini
eff = ""
for x in effi:
    if x == "%":
        break
    else:
        eff = eff + x
eff = int(eff)

BTU = (goil/42)*((100-eff)/100)*5800000
print(f"BTU: {BTU:.2f}")