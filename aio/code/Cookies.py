'''infile=open('cookiesin.txt','r')
t, s = map(int,infile.readline().strip().split())
c1, s1 = map(int,infile.readline().strip().split())
c2, s2 = map(int,infile.readline().strip().split())
temp = None
t1=0
t2=0
tc1=False
tc2 = False
t12=0
t21=0
tot = s*t
while t1*s<c1:
    t1+=1
if (t-t1)*s1>c1:
    temp = 'c1'
    tot = (t-t1)*s1-c1+t*s
    tc1 = True

while t2*s<c2:
    t2+=1
if (t-t2)*s1>c1:
    tc2 = True
    if (t-t2)*s2>tot:
        temp = 'c2'
        tot = s*t+(t-t2)*s1-c1
while t12*(s+s1)+t1*s<c2+c1:
    t12+=1
if t*s+(t-t1)*s1+(t-t1-t12)*s2-c1-c2>tot:
        tot=t*s+(t-t1)*s1+(t-t1-t12)*s2-c1-c2
while t21*(s+s2)+t2*s<c2+c1:
    t21+=1
if (t-t2-t21)*s1>=c1 and t*s+(t-t2)*s2+(t-t2-t21)*s1-c1-c2>tot:
    temp = 'c21'
    tot = t*s+(t-t2)*s2+(t-t2-t21)*s1-c1-c2

out = open('cookiesout.txt','w')
out.write(str(tot))
out.close()
'''
infile=open('cookiesin.txt','r')
outfile=open('cookiesout.txt','w')
d,c0=map(int,infile.readline().strip().split())
p1,c1=map(int,infile.readline().strip().split())
p2,c2=map(int,infile.readline().strip().split())
#Eddie Gao

def first(d,c0,p1,c1,p2,c2):
    if p1%c0!=0:
        day=p1//c0+1
    else:
        day=p1//c0
    left=(day*c0)-p1
    vel=c0+c1
    d-=day
    total=(d*vel)+left
    return total

def second(d,c0,p1,c1,p2,c2):
    if p2%c0!=0:
        day=p2//c0+1
    else:
        day=p2//c0
    left=(day*c0)-p2
    vel=c0+c2
    d-=day
    total=(d*vel)+left
    return total
    
def both1(d,c0,p1,c1,p2,c2):
    if p2%c0!=0:
        day=p2//c0+1
    else:
        day=p2//c0
    left=(day*c0)-p2
    vel=c0+c2
    d-=day
    p1-=left
    if p1%vel!=0:
        day=p1//vel+1
    else:
        day=p1//vel
    left=(day*vel)-p1
    vel+=c1
    d-=day
    total=(d*vel)+left
    return total

def both2(d,c0,p1,c1,p2,c2):
    if p1%c0!=0:
        day=p1//c0+1
    else:
        day=p1//c0
    left=(day*c0)-p1
    vel=c0+c1
    d-=day
    p2-=left
    if p2%vel!=0:
        day=p2//vel+1
    else:
        day=p2//vel
    left=(day*vel)-p2
    vel+=c2
    d-=day
    total=(d*vel)+left
    return total

sol1=d*c0                                                           #don't buy anyting
sol2=first(d,c0,p1,c1,p2,c2)                                        #only buy the first factory
sol3=second(d,c0,p1,c1,p2,c2)                                       #only buy the second factory
sol4=max(both1(d,c0,p1,c1,p2,c2),both2(d,c0,p1,c1,p2,c2))           #buy both factory
    
answer=max(sol1,sol2,sol3,sol4)
outfile.write(str(answer))
outfile.close()
