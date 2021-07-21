'''
infile = open('tennisin.txt','r')
B, N = map(int, infile.readline().split())
A = list(map(int,infile.readline().split()))
i,b=0,1
while True:
    if A[b-1]>0:
        A[b-1]-=1
        i+=1
        if i==N:
            break
    b+=1
    if b>B:
        b-=B

outfile=open('tennisout.txt','w')
outfile.write(str(b))
outfile.close()
'''
'''
infile = open('tennisin.txt','r')
B, N = map(int, infile.readline().split())
A = list(map(int,infile.readline().split()))
li=[i for i in range(B)]
li2=[]
i,b=N,B
while True:
    if i>b:
        for j in li:
            if A[j]==0:
                b-=1
            else:
                A[j]-=1
                if A[j]==0:
                    li2.append(j)
        for k in li2:
            li.remove(k)
        li2.clear()
        i-=b
        b=len(li)
    else:
        ans=li[i-1]+1
        break
        

outfile=open('tennisout.txt','w')
outfile.write(str(ans))
outfile.close()
'''
infile = open('tennisin.txt','r')
B, N = map(int, infile.readline().split())
A = list(map(int,infile.readline().split()))
li=[i for i in range(B)]
a=sorted(A)
li2=[]
i,b=N,B
for x in range(B):
    mod=i%b
    if i<=a[x]*b:
        if mod:
            ans=mod
        else:
            ans=b
    else:
        ii=i
        i-=a[x]*b
        for j in range(a):
            if mod:
                A[j]-=ii//b+1
            else:
                A[j]-=ii//b
            if A[j]==0:
                li2.append(A[j])
                b-=1
        for j in li2:
            A.remove(j)
        for j in a:
            if a[j]>0:
                if mod:
                    a[j]-=ii//b+1
                else:
                    a[j]-=ii//b
                if a[j]==0:
                    a[j]=-1
        

outfile=open('tennisout.txt','w')
outfile.write(str(ans))
outfile.close()