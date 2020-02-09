a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
if a>b:
    max=a
else: max=b
if c>max:
    max=c
else: None
print(max)
k=max**3
print('k=',k)
