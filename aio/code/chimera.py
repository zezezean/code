infile=open('chimin.txt','r').readlines()
l,str1,str2,strt=infile
x,p=0,0
outfile=open('chimout.txt','w')
for i in range(len(strt)):
    if p!=2:
        if str1[i]!=strt[i]:
            if str2[i]==strt[i]:
                if p!=0: x+=1
                p=2
            else: x=-1; break
    if p!=1:
        if str2[i]!=strt[i]:
            if str1[i]==strt[i]:
                if p!=0: x+=1
                p=1
            else: x=-1; break
if x==-1:
    outfile.write('PLAN FOILED')
else:
    outfile.write('SUCCESS\n'+str(x))
outfile.close()