infile=open('sitin.txt','r')
a,b=infile.readline().split()
a=int(a)
b=int(b)
c=infile.readline()
c=int(c)
if a*b<=c:
    answer=str(a*b)+' '+str(c-a*b)
else:
    answer=str(c)+' '+str(0)
outfile=open('sitout.txt','w')
outfile.write(answer)
outfile.close()
'''
this is so awesome








































































'''
