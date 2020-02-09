a=int(input('a='))
x=int(input('x='))
if x>abs(a):
   y=(x**2)**3+((x**2)**-3)
elif 3<x<abs(a):
   y=(abs(x**2/a))*((x**2)+a)**3
else:
    y=((x**2)+a)**3
print('y=',y)
