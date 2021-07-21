RULES = {
  ('scissors', 'scissors') : '00',
  ('scissors', 'paper'): '10',
  ('scissors', 'rock'): '01',
  ('paper', 'paper'): '00',
  ('paper', 'rock'): '10',
  ('rock', 'rock'): '00'
}
N = int(input())
A=input().split()
B=input().split()
sA,sB=0,0
for i in range(N):
    if (A[i], B[i]) in RULES:
      result = RULES[(A[i], B[i])]
      if result == '10':
          sA+=1
      elif result=='01':
          sB+=1
    else:
      result = RULES[(B[i], A[i])]
      if result == '10':
          sB+=1
      elif result=='01':
          sA+=1
print(f"{sA} {sB}")