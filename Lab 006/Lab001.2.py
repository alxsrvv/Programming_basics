k=int(input('Введіть число \n'))
n=22+10
maxi=k
for i in range(1,n):
    k=int(input('Введіть число \n'))
    if k>maxi:
        maxi=k
print('Найбільше число',maxi)
