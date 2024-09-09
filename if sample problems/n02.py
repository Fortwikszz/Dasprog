wei = int(input("Input weight (pounds): "))
hei = int(input("Input height (inches): "))

bmi = (703*wei)/(hei**2)

match bmi:
    case bmi if bmi < 18.5:
        print("Underweight")
    case bmi if bmi < 25:
        print("Normal")
    case bmi if bmi < 30:
        print("Overweight")
    case bmi if bmi >= 30:
        print("Obese")