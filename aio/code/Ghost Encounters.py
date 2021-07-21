'''timeout
infile = open('ghostin.txt','r')
N, K = infile.readline().split()
N = int(N)
x={}
t={}
mx={}
tmx = 0
for i in range(0, N):
    x[i],t[i]=infile.readline().strip().split()
    x[i] = int(x[i])
    t[i] = int(t[i])
for i in range(N-1, -1, -1):
    for j in range(i-1,-1,-1):
        if (x[i]-x[j])*int(K)==t[i]-t[j]:
            if i not in mx:
                mx[i]=1
            mx[i]+=1
for i in range(0,N):
    if i in mx:
        if int(mx[i]) > tmx:
            tmx = int(mx[i])
outfile = open('ghostout.txt','w')
outfile.write(str(tmx))
outfile.close()
'''
infile=open("ghostin.txt","r").readlines()
n,k=[int(i) for i in infile[0].split()]
X=[]
T=[]
for line in infile[1:]:
    x,t=[int(i) for i in line.split()]
    X.append(x)
    T.append(t)
A=[k*x for x in X]
d={}
for i in range(n):
    shift=T[i]-A[i]
    if shift not in d:
        d[shift]=1
    else:
        d[shift]+=1
ans=max(d.values())
open("ghostout.txt","w").write(str(ans))