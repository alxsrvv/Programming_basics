string = input('Input line: ')
count=0
for i in string:
    if ord(i)>=97 and ord(i)<=122:
        count+=1
print(count)

words = string.split(' ')
letter_max=0
for i in words:
    letter_count=0
    for j in i:
        letter_count+=1
    if letter_max <= letter_count:
        letter_max=letter_count
        max_word = i
print(max_word)

words_arr = []
words2 = string. split(' ')
for i in words2:
    if ord(i[0])>=97 and ord(i[0])<=122:
        words_arr.append(i+' ')
new_string = ''.join(words_arr)
print(new_string)



        


        
