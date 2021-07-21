infile=open('addin.txt','r')
a,b=map(int,infile.readline().split())
open('addout.txt','w').write(str(a+b))