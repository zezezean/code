infile=open("surfin.txt",'r').readlines()
r,c=map(int, infile[0].split())
grid=infile[1:]
good=[(r-1,c-1)]
ans=r*c
def up(current):
    row=current[0]
    col=current[1]
    if row>0 and grid[row-1][col]=="v":
        good.append((row-1,col))
def le(current):
    row=current[0]
    col=current[1]
    if col>0 and grid[row][col-1]==">":
        good.append((row,col-1))
while good:
    cur=good.pop()
    ans-=1
    up(cur)
    le(cur)
print(r,c,grid,good)
outfile=open("surfout.txt",'w')
outfile.write(str(ans))
outfile.close()
