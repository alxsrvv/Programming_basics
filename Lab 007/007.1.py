import random

m=int(input('m='))
k=int(input('k='))

while k>10 or k<3:
    k=int(input('k='))

i=0
j=0
while i<m:
    j=0
    while j<k and i<m:
        print(random.randint(-444,333),end=' ')
        j+=1
        i+=1
    print()
