def zero(arr):
        '''
        Every even element of arr are changing on zero
        Parameters:
        arr
        '''
        for i in range(len(arr)):
                if arr[i] % 2 == 0:
                        arr[i] = 0
a = [1,2,3,4,5,6,7,8,9]
zero(a)
print(a)
