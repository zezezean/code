infile = open('hippoin.txt','r').readlines()
n,a,b,c=[int(i) for i in infile]
if a-1 > n-c:
    ans=a-1+max(b-a-1,c-b-1,n-c)
else:
    ans=n-c+max(a-1,b-a-1,c-b-1)
open('hippoout.txt','w').write(str(ans))