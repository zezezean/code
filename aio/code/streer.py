infile=open('streetin.txt','r')
n,k=map(int,infile.readline().split())
if not (n-k)%(k+1): ans =n//(k+1)
else: ans=(n-k)//(k+1)+1
outfile = open('streetout.txt','w')
outfile.write(str(ans))
outfile.close()