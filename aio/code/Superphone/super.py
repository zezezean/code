lines=open("phonein.txt","r").readlines()
l,f,r=[int(i) for i in lines[1].split()]
time_lhs=f+r
time_rhs=l

for line in lines[2:-1]:
    l,f,r=[int(i) for i in line.split()]
    time_lhs=min(time_lhs, time_rhs+f)
    time_rhs=min(time_rhs, time_lhs+f)
    time_lhs,time_rhs=time_rhs+r,time_lhs+l
    
f=int(lines[-1])
time_rhs=min(time_rhs,time_lhs+f)
open("phoneout.txt","w").write(str(time_rhs))