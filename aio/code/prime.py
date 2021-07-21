N = int(open('primein.txt','r').readline())
outfile=open('primeout.txt','w')
li=[]
outfile.write('2'+'\n')
A=True
for i in range(3,N+1,2):
    for j in li:
        A=True
        if j*j>i:
            break
        if not i%j:
            A=False
            break
    if A:
        li.append(i)
        outfile.write(str(i)+'\n')

outfile.close()