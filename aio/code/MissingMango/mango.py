l1,l2,d1,d2=map(int,open("manin.txt",'r').readline().strip().split())
p1=set([l1-d1,l1+d1])
p2=set([l2-d2,l2+d2])
ans=[str(i) for i in p1.intersection(p2)]
open("manout.txt",'w').write(ans[0])