infile = open('manin.txt','r')
n,w = map(int,infile.readline().split())
li = [0]
#p=[0]*(n+1)
ans=0
for i in range(n):
    li.append(int(infile.readline().strip()))
for i in range(1,n+1):
    li[i]=li[i-1]+li[i]
for i in range(0,n-w+1):
    ans=max(ans,li[i+w]-li[i])
outfile = open('manout.txt','w')
outfile.write(str(ans))
outfile.close()