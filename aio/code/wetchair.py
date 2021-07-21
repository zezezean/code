infile= open('chairsin.txt','r')
c,n,k=map(int,infile.readline().strip().split())
line = infile.readline().strip()
wide = 0
w,d,i,j=0,0,0,0
ans= 100001
while i<c:
    while (d<n-k or w+d<n) and j<c:
        if line[j]=='w':
            w+=1
        else:
            d+=1
        j+=1
    if w+d>=n and d>=n-k:
        ans=min(ans,j-i)
    if line[i]=='w':
        w-=1
    else:
        d-=1
    i+=1
outfile = open('chairsout.txt','w')
outfile.write(str(ans))
outfile.close()