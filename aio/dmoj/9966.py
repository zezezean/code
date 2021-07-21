'''a,b = [int(i) for i in input().split()]
tot=0
def re(num):
    if '2' in num or '3' in num or '4' in num or '5' in num or '7' in num:
        return False
    else:
        return func(num)
def func(n):
    if n == '0' or n == '1' or n == '8':
        return True
    elif not len(n)%2:
        n1 = n[0:(int(len(n)/2))]
        #n2 = n[int(len(n)/2):len(n):-1]
        n2 = n[int(len(n)-1):int(len(n)/2)-1:-1]
        n2.replace('6',')')
        n2.replace('9','6')
        n2.replace(')','9')
        if n1 == n2:
            return True
    elif len(n)%2 and int(n)>9:
        n0=n[int((len(n)+1)/2)]
        n1 = n[0:int((len(n)-1)/2)]
        #n2 = n[int((len(n)+1)/2):len(n):-1]
        n2 = n[len(n)-1:int((len(n)+1)/2)-1:-1]
        n2.replace('6',')')
        n2.replace('9','6')
        n2.replace(')','9')
        if (n0 == '0' or n0 == '1' or n0 == '8') and n1 == n2:
            return True
    return False
for i in range(a,b+1):
    if re(str(i)):
        tot+=1
print(str(tot))'''

a,b = [int(i) for i in input().split()]
tot=0
    
for i in range(a,b+1):
    i=str(i)
    if '2' in i or '3' in i or '4' in i or '5' in i or '7' in i:
        pass
    else:
        if i == '0' or i == '1' or i == '8':
            tot+=1
        elif not len(i)%2:
            n1 = i[0:(int(len(i)/2))]
            #n2 = n[int(len(n)/2):len(n):-1]
            n2 = i[int(len(i)-1):int(len(i)/2)-1:-1]
            n2.replace('6',')')
            n2.replace('9','6')
            n2.replace(')','9')
            if n1 == n2:
                tot+=1
        elif len(i)%2 and int(i)>9:
            n0=i[int((len(i)+1)/2)]
            n1 = i[0:int((len(i)-1)/2)]
            #n2 = n[int((len(n)+1)/2):len(n):-1]
            n2 = i[len(i)-1:int((len(i)+1)/2)-1:-1]
            n2.replace('6',')')
            n2.replace('9','6')
            n2.replace(')','9')
            if (n0 == '0' or n0 == '1' or n0 == '8') and n1 == n2:
                tot+=1
print(str(tot))
'''
a,b = [int(i) for i in input().split()]

tot = 0

for x in range(a, b+1):
  skip = False
  num = str(x)
  rotated = ""
  
  for y in range(len(num)):
    if num[y] == "6":
      rotated += "9"
    elif num[y] == "9":
      rotated += "6"
    elif num[y] == "8":
      rotated += "8"
    elif num[y] == "1":
      rotated += "1"
    elif num[y] == "0":
      rotated += "0"
    else:
      skip = True
      break
  
  if number == rotated[::-1] and not skip:
    tot+=1
    
print(str(tot))
'''