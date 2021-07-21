lines=open('alienin.txt','r')
n,k = map(int,lines[0].split())
ans=0
w=0
i,j=1,2
while i<n:
    while j<n+1:
        if lines[j]-lines[i]<k:
            w+=1
            j+=1
        else:
            ans=max(ans,w)
            i+=1
            j+=1
outfile = open('alienout.txt','w')
outfile.write(str(ans))
outfile.close()
        