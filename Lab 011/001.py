file = open('.\InfoaboutStud.txt','r')
lines = file.readlines()
for i in lines:
    row_data = i.split(' ')
    town = row_data[3]
    mark = int(row_data[4])
    if town == 'Київ' and mark > 180:
        print(i)
file.close()
