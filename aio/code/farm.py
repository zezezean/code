infile = open('farmin.txt','r')
lines = infile.readlines()
count=0
n=int(lines[0])
line = [int(i) for i in lines[1].split()]
a=[line[0]]
for i in range(1,n):
    a.append(a[i-1]+line[i])
line.reverse()
b=[line[0]]
for i in range(1,n):
    b.append(b[i-1]+line[i])
i,j=0,0
while i<n and j<n:
    if a[i]==b[j]:
        i+=1
        j+=1
        count+=1
    elif a[i]>b[j]:
        j+=1
    else:
        i+=1
outfile=open('farmout.txt','w')
outfile.write(str(n-count))
outfile.close()
'''
aa=set(a)
bb=set(b)
in = aa.intersection(bb)
len(in)
'''