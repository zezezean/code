infile=open('cocoin.txt','r')
cir1 = list(map(float,infile.readline().split()))
cir2 = list(map(float,infile.readline().split()))
dis=((abs(cir1[0]-cir2[0]))**2+(abs(cir1[1]-cir2[1]))**2)**(0.5)
if dis>cir1[2]+cir2[2] or dis+min(cir1[2],cir2[2])<max(cir1[2],cir2[2]):
    ans='no'
else:
    ans='yes'
outfile=open('cocoout.txt','w')
outfile.write(ans)
outfile.close()