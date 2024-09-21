x1, y1 = input().split()
xs, ys = input().split()
xf, yf = input().split()
x1, y1 = int(x1), int(y1)
xs, ys = int(xs), int(ys)
xf, yf = int(xf), int(yf)

jarling = ((xs-x1)**2+(ys-y1)**2)**0.5
jarjal = abs((xf-xs)**2+(yf-ys)**2)**0.5

if jarling <= jarjal:
    print("No")
else:
    print("Yes")