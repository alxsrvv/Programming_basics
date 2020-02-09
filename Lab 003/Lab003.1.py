a=1000
n=int(input('n='))
b=10**n
y=((a-b)**4)-((a**4)-4*(a**3)*b)/6*(a**2)*(b**2)-4*a*(b**3)+b**4
print('y=',round(y,10))
