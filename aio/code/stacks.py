infile = open('stacksin.txt', 'r')
outfile = open('stacksout.txt', 'w')
string = ''
li = []
for i in infile:
    i=i.strip()
    if not i.isalpha():
        li.append(i)
        string +=' '.join(li)+'\n'

    elif i == 'p':
        li.pop()
        if len(li)== 0:
            string+='stack is empty!\n'
        else:
            string +=' '.join(li)+'\n'

    elif i == 'q':
        break
    
outfile.write(string)

outfile.close()