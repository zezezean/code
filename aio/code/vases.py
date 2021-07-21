N=open("vasesin.txt",'r').readline().strip()
out=open("vasesout.txt",'w')
N=int(N)
x=0
for i in range(1, N+1):
    for j in range(1, N-i+1):
        if i!=j and j!=N-i-j and i!=N-i-j and N-i-j>0:
            x=1
            break
    if x == 1:
        break
if x == 0:
    out.write('0 0 0')
else:
    ans=str(N-i-j)+' '+str(i)+' '+str(j)
    out.write(str(ans))
out.close()