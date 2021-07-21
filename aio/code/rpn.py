infile = open('rpnin.txt', 'r')
outfile = open('rpnout.txt', 'w')
string = ''
li = []
for i in infile:
    i=i.strip()
    if i == '+':
        x = int(li[-2])+int(li[-1])
        del li[-2:]
        li.append(str(x))
        string +=' '.join(li)+'\n'
    elif i == '-':
        x = int(li[-2])-int(li[-1])
        del li[-2:]
        li.append(str(x))
        string +=' '.join(li)+'\n'
    elif i == '*':
        x = int(li[-1])*int(li[-2])
        del li[-2:]
        li.append(str(x))
        string +=' '.join(li)+'\n'
    elif i == '/':
        x = int(li[-2])/int(li[-1])
        x=int(x)
        del li[-2:]
        li.append(str(x))
        string +=' '.join(li)+'\n'
    elif i == 'swap':
        li[-1],li[-2]=li[-2],li[-1]
        string +=' '.join(li)+'\n'
    elif i == 'p':
        li.pop()
        if not li:
            string+='stack is empty!\n'
        else:
            string +=' '.join(li)+'\n'
    elif i == 'dup':
        li.append(li[-1])
        string +=' '.join(li)+'\n'
    elif i == 'q':
        break
    else:
        li.append(i)
        string +=' '.join(li)+'\n'
    x=0
    
outfile.write(string)

outfile.close()