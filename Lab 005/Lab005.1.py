import math
xn=-0.31
xk=0.61
dx=0.3
x=xn
a=8
while x<=xk:
    y=a*(x**(5/2))+a**(x/2)
    print('x=',x)
    print('y=',y)
    x+=dx
