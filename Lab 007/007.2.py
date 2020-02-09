arr=[]
n = int(input('Enter n:'))
for i in range(n):
    arr.append(int(input('Enter element:')))
min_el=arr[0]
for i in range(n):
    if arr[i]<=min_el:
        min_el=arr[i]
print('Min is ', min_el)

index_first=0
index_last=0
for i in range(n-1,-1,-1):
    if arr[i]>0:
        index_first=i
for i in range(n):
    if arr[i]>0:
        index_last=i
Sum=0
for i in range(index_first+1,index_last):
    Sum+=arr[i]
print('Sum is ',Sum)
