x, y = input("(X,Y): ").split()
x, y = float(x), float(y)

match x, y:
    case x, y if x == 0 and y == 0:
        print("(0.0, 0.0) is on the center")
    case x, y if (x > 0 or x < 0) and y == 0:
        print(f"({x:.1f}, 0.0) is on the x-axis")
    case x, y if x == 0 and (y > 0 or y < 0):
        print(f"(0.0, {y:.1f}) is on the y-axis")
    case x, y if x > 0 and y > 0:
        print(f"({x:.1f}, {y:.1f}) is in Quadrant I")
    case x, y if x < 0 and y > 0:
        print(f"({x:.1f}, {y:.1f}) is in Quadrant II")
    case x, y if x < 0 and y < 0:
        print(f"({x:.1f}, {y:.1f}) is in Quadrant III")
    case x, y if x > 0 and y < 0:
        print(f"({x:.1f}, {y:.1f}) is in Quadrant IIII")