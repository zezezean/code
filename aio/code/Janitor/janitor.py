lines=open("janitorin.txt",'r').readlines()
r,c,q=[int(i) for i in lines[0].split()]
grid=[[int(i) for i in line.split()] for line in lines[1:1+r]]
tiles=[[int(i) for i in line.split()] for line in lines[1+r:1+r+q]]

def is_peak(cell):
    row, col = cell
    h=grid[row][col]
    if row>0 and grid[row-1][col]>h:
        return False
    if row<r-1 and grid[row+1][col]>h:
        return False
    if col>0 and grid[row][col-1]>h:
        return False
    if col<c-1 and grid[row][col+1]>h:
        return False
    return True

def peaks(cell):
    row,col=cell
    count=0
    if is_peak((row,col)):
        return 1
    if row>0 and is_peak((row-1,col)):
        count+=1
    if row<r-1 and is_peak((row+1,col)):
        count+=1
    if col>0 and is_peak((row,col-1)):
        count+=1
    if col<c-1 and is_peak((row,col+1)):
        count+=1
    return count

count=0
for i in range(r):
    for j in range(c):
        if is_peak((i,j)):
            count+=1
outfile= open("janitorout.txt","w")
outfile.write(str(count)+"\n")
for tile in tiles:
    i,j,h=tile
    i,j=i-1,j-1
    before=peaks((i,j))
    grid[i][j]=h
    after=peaks((i,j))
    count=count+after-before
    outfile.write(str(count)+'\n')
outfile.close()