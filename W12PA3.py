# Take an input of a complete e-mail address and print the roll number before @ and
#institute name after @ address but before first dot in the e-mail address.

r_number = input()
print(r_number.split('@')[0], r_number.split('@')[1].split('.')[0], end='')


'''
# Past Week-12 Prog assignment. It is different from the one given for Oct-2022. 

for t in range(int(input())):
  n = int(input())
  m = [int(j) for j in input().split()]
  mn,mnidx,mx,mxidx=m[0],0,m[0],0
  for i in range(n):
    if m[i]<mn:
      mn=m[i]
      mnidx=i
    if m[i]>mx:
      mx=m[i]
      mxidx=i
    b = max(mnidx,mxidx)
    c = min(mnidx,mxidx)
  print(min([c-b+1+n,b+1,n-c]))

  '''

