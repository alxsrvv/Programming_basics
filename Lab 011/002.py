import re

def LetterIsVowel(l):
    if l=='a' or l=='o' or l=='y' or l=='u' or l=='e'  or l=='i':
        return 1
    else:
        return 0
    
file = open('input.txt','r')
lines = file.readlines()
newfile = open('output.txt','w')
for i in lines:
    words = re.findall(r"[\w']+",i)
    newline=''
    for j in words:
        vowels = []
        flag=1
        for k in j:
            if LetterIsVowel(k):
                if k not in vowels:
                    vowels.append(k)
            if len(vowels)==3:
                flag=0
        if flag==1:
            newline+=j+' '
    newfile.write(newline+'\n')
    
newfile.close()
    
        
    
    
