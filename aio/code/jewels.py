infile= open('jewelsin.txt','r')
lines=infile.readlines()
n=int(lines[0])
s=lines[1].strip()
rs = s*2
pre=0
cur=1
ans=0
for i in range(1,2*n):
    if rs[i]==rs[i-1]:
        cur+=1
    else:
        if pre + cur > ans:
            ans = pre+cur
        pre = cur
        cur = 1
if cur>1:
    if cur+pre>ans:
        ans=cur+pre
if ans==2*n:
    ans=n
outfile= open('jewelsout.txt','w')
outfile.write(str(ans))
outfile.close()