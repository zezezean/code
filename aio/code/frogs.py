infile = open('frogin.txt','r')
n=int(infile.readline().strip())
h=[int(i) for i in infile.readlines()]
minf=[h[0]]
for i in range(1,n):
    minf.append(min(minf[i-1],h[i]))
mins=[]
#mint = minf[-1]
mint = h[-1]
for i in reversed(h):
    mint=min(mint, i)
    mins.append(mint)
mins.reverse()

ans=0
for i in range(n):
    if minf[i]<h[i] and mins[i]<h[i]:
        ans=max(ans,h[i]-minf[i]+h[i]-mins[i])
outfile = open('frogout.txt','w')
outfile.write(str(ans))
outfile.close()