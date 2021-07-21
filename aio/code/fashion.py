a = int(open('fashin.txt','r').readline())
s1=int(a/100)
a%=100
s2=int(a/20)
a%=20
s3=int(a/5)
a%=5
ans = s1+s2+s3+a
outfile = open('fashout.txt','w')
outfile.write(str(ans))
outfile.close()