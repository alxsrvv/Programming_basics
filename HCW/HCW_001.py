from math import factorial
from math import exp

def NonRec(x,eps):
 	s = 1
 	term = 1
 	i = 0
 	while (abs(term)>eps):
 		term = term*(x/(i+1))
 		s+=term
 		i+=1
 	return s

def NonRec2(x,n):
	s = 1
	for i in range(1,n+1):
		x+=x**i/factorial(i)
	return s

def Rec(x,n):
	if n == 0:
		return 1
	else:
		return x**n/factorial(n)+Rec(x,n-1)

x = float(input('x = '))
eps = float(input('eps = '))

n = 0
term = 1
while (abs(term)>eps):
	term = term*x/(n+1)
	n+=1
print('number of terms = ',n)

y1 = NonRec(x,eps)
y2 = Rec(x,n)
y3 = exp(x)
y4 = NonRec2(x,n)
error1 = abs(y1-y3)
error2 = abs(y2-y3)
error3 = abs(y4-y3)

print('y1(NonRec) = ',y1)
print('y2(NonRec2) = ',y4)
print('y(math) = ',y3)
print('y(Rec) = ',y2)
print('What about errors?')
print('error1 = ',error1)
print('error2 = ',error2)
print('error3 = ',error3)
