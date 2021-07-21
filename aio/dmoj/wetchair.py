infile= open('chairsin.txt','r')
c,n,k=map(int,infile.readline().strip().split())
line = infile.readline().strip()
w,d=k,n
wide = 0
i,j=0,0
ans= None
while i<c:
    while j<c:
        if w<0:
            break
        if line[j]=='w':
            w-=1
            wide+=1
            d-=1
        if line[j]=='d':
            wide+=1
            d-=1
        if d==0:
            ans = min(ans,wide)
            break
        j+=1
    i+=1
outfile = open('chairsout.txt','w')
outfile.write()
outfile.close()