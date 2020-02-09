import random

def show(arr):
    for i in range(len(arr)):
        print()
        for j in range(len(arr)):
            print(arr[i][j], end=' ')
            
def fill(arr):
    '''
    Every element of arr will be filled randomly (from 0 to 100)
    Parameters:
    arr
    '''
    for i in range(len(arr)):
        for j in range(len(arr)):
            arr[i][j] = random.randint(0,101)

def min(arr):
    '''
    searching for the minimal element of arr
    Parameters:
    arr
    '''
    min=arr[0][0]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] <= min:
                min = arr[i][j]
    return min

def max(arr):
    '''
    searching for the maximal element of arr
    Parameters:
    arr
    '''
    max=arr[0][0]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] >= max:
                max = arr[i][j]
    return max

n = int(input('Enter diagonal of array= '))
a = [[0]*n for i in range(n)]
fill(a)
show(a)
print()

m = int(input('Enter number of row= '))
minimum=min(a)
maximum=max(a)

for i in range(len(a)):
    a[m][i] = int((minimum+maximum)/2)
show(a)
