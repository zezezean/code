def p3int(v):
    if v<=9:
        print('  '+str(v), end='')
    elif v<=99:
        print(' '+str(v),end='')
    else:
        print(str(v),end='')


a,b = [int(i) for i in input().split()]
c = a
print("Sun Mon Tue Wed Thr Fri Sat")
for i in range(1,c):
    print("    ",end='')
for i in range(1, b+1):
    p3int(i)
    c+=1
    if c == 8 or i == b:
        print("\n", end='')
        c = 1
    else:
        print(" ",end='')
'''
s,d = [int(i) for i in input().split()]
print('Sun Mon Tue Wed Thr Fri Sat')
string=''
space = '  '
for i in range(1,d+s):
    if i-s+1==10:
        space=' '
    if i-s+1 == 100:
        space = ''
    if i<s:
        string+=space*2
    elif not i%7:
        string=string+space+str(i-s+1)+'\n'
    else:
        string=string+space +str(i-s+1)+' '
if string[-1]==' ':
    string = string[:-1]+'\n'
print(str(string))
'''