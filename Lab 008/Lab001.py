import random

n = int(input('number of rows = '))
m = int(input('number of columns = '))
while m < 3:
	m = int(input('number of columns = '))
a = int(input('from this number = '))
b = int(input('to this number = '))
while b<a:
   b = int(input('to this number'))
arr = [[0]*m for i in range(n)]
for i in range(n):
	for j in range(m):
		arr[i][j] = random.randint(a,b)
		print(arr[i][j],end=' ')
	print()

max = 0
for i in range(n):
	for j in range(m):
		if max < arr[i][2]:
			max = arr[i][2]
print('Maximum value of third column = ',max)

sum = 0
for i in range(n):
	if arr[0][i] % 2 == 1:
		sum+=arr[0][i]
print('Amount of odds = ',sum)