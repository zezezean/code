lines=open('alienin.txt','r').readlines()
n,k = map(int,lines[0].split())
ans=1
i,j=1,2
while i<n:
    while j<n+1:
        if int(lines[j])-int(lines[i])<k:
            j+=1
        else:
            i+=1
        if j-i>ans:
            ans=j-i
    i+=1
outfile = open('alienout.txt','w')
outfile.write(str(ans))
outfile.close()
        