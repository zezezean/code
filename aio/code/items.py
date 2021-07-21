li = []
while True:
    it = input('Item: ').lower()
    if not it: break
    if ('-'+it) not in li: li.append('-'+ it)
    else: print(f"You've already got {it}")
print(f"Your have purchased {len(li)} items.\nThe items you have purchased are: ")
print('\n'.join(li))