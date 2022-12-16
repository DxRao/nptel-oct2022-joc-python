# Reverse the integer number input

n=int(input()) 
rev=0
while(n>0):
   remainder = n%10
   rev=(rev*10)+ remainder 
   n=n//10 
print(rev, end='')


'''
n=int(input("Enter number: ")) 
rev=0
while(n>0):
   dig=n%10
   rev=rev*10+dig 
   n=n//10 
print("Reverse of the number: ",rev)
'''


'''

# Different problem from above given in past as Week-12 prog assignment.

n=[]
a=0
for i in (input().split()):
  n.append(int(i))
  a+=int(i)
if a%len(n)==0:
  c=0
  for i in n:
    if i>a//len(n):
      c+=i-a//len(n)
  print(c,end='')
else:
  print(-1,end='')
  
'''

