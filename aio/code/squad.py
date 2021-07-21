infile=open('cavalryin.txt','r')
n= int(infile.readline())
B=True
dic={}
for i in range(n):
    line=int(infile.readline().strip())
    if line not in dic:
        dic[line]=1
    else:
        dic[line]+=1
for i in dic:
    if dic[i]%i:
        print(str(i))
        B=False
        break
outfile=open('cavalryout.txt','w')
if B:
    outfile.write('YES')
else:
    outfile.write('NO')
outfile.close()
