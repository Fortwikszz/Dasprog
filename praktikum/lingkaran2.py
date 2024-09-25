x1, y1 = input().split()
xs, ys = input().split()
xf, yf = input().split()
x1, y1 = int(x1), int(y1)
xs, ys = int(xs), int(ys)
xf, yf = int(xf), int(yf)

jarling = abs((xf-x1)**2+(yf-y1)**2)
jarjal = abs((xf-xs)**2+(yf-ys)**2)

if jarling <= jarjal:
    print("No")
else:
    print("Yes")