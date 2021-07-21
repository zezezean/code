infile=open('antsin.txt','r').readlines()
d=int(infile[0])
ant=[]
s=False
ans=0
for i in range(2,d+1):
    a=int(infile[i])-int(infile[i-1])
    ant.append(a)
    if s and ant[i-2]<=0:
        ans+=1
        s=False
    elif ant[i-2]>0:
        s=True
    if i==d and s:
        ans+=1
open('antsout.txt','w').write(str(ans))