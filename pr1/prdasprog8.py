populus = int(input("Populasi: "))

toilet = populus // 3
old = 15 * 14 * toilet
new = 2 * 14 * toilet

cost = toilet * 150
save = old - new

print(f"Water saved per day: {save:.2f} liters")
print(f"Total installation cost: ${cost}")