x1, y1 = input().split()
xs, ys = input().split()
xf, yf = input().split()
x1, y1 = int(x1), int(y1)
xs, ys = int(xs), int(ys)
xf, yf = int(xf), int(yf)

detik = ((xf-xs)**2 + (yf-ys)**2)**(1/2)
grad = (yf-ys)/(xf-xs)

grads = (ys-y1)/(xs-x1)
gradf = (yf-y1)/(ys-y1)

grad2 = -1/grad

if grad == 0 or grad2 == 0:
    print("Rawr")
elif ((grads < gradf) and (grads > grad2 < gradf)) or ((grads > gradf) and (grads < grad2 > gradf)):
    print("Yes")
    
else:
    x = ((grad*(-xs)+ys)-(grad2*(-x1)+y1))/((-grad)-(-grad2))
    y = (grad2*x)+(grad2*(-x1)+y1)
    
    ling = ((y-y1)**2+(x-x1)**2)**(1/2)
    dist = ((y-ys)**2+(x-xs)**2)**(1/2)
    
if ling >= dist:
    print("Yes")
else:
    print("No")