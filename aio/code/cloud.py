infile=open('cloudin.txt','r')
lines=infile.readlines()
N,K=map(int,lines[0].split())
li=[0]*N
ans=100000000001
for i in range(1,N):
    li[i]=li[i-1]+int(lines[i])
for i in range(0,N-K):
    ans=min(ans,li[i+K]-li[i])
outfile=open('cloudout.txt','w')
outfile.write(str(ans))
outfile.close()