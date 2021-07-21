'''infile = open('tagin.txt','r')
n, m = map(int, infile.readline().split())
r=[1]
b=[2]
tags=infile.readlines()
for i in range(1,m+1):
    if tags[i][0] in r:
        r.append(tags[i][1])
    else:
        b.append(tags[i][1])
        

outfile=open('tagout.txt','w')
outfile.write(f"{len(r)} {len(b)}")
outfile.close()
'''
infile = open('tagin.txt','r')
n, m = map(int, infile.readline().split())
r=[-1]+[1]+[2]+[0]*(n-2)
R,B=0,0
tags=[i.strip().split() for i in infile]
for i in range(m):
    if r[int(tags[i][0])]==1:
        r[int(tags[i][1])]=1
    else:
        r[int(tags[i][1])]=2
for i in r:
    if i == 1:
        R+=1
    elif i==2:
        B+=1

outfile=open('tagout.txt','w')
outfile.write(str(R) + " " + str(B))
outfile.close()