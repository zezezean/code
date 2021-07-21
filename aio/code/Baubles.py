'''R,B,S,r,b = map(int,input('').split())
xr=R-r
xb=B-b
if xr < 0:
    S = S+xr
    R=r
if xb < 0:
    S = S+xb
    B=b
sol = S+1
if xr >= 0 and xb >= 0:
    if b==0:
        sol = xr+S+1
    elif r==0:
        sol = xb +S+1
    elif xr>xb:
        sol = xb+S+1
    else:
        sol = xr+S+1
if sol < 0:
    sol=0
print(str(sol))'''
R,B,S,r,b = map(int,open('baublesin.txt','r').readline().split())
xr=R-r
xb=B-b
if xr < 0:
    S = S+xr
    R=r
if xb < 0:
    S = S+xb
    B=b
sol = S+1
if xr >= 0 and xb >= 0:
    if b==0:
        sol = xr+S+1
    elif r==0:
        sol = xb +S+1
    elif xr>xb:
        sol = xb+S+1
    else:
        sol = xr+S+1
if sol < 0:
    sol=0
outfile=open('baublesout.txt','w')
outfile.write(str(sol))
outfile.close()