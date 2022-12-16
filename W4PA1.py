L = []
n = int(input())
k = int(input())

L = [None] * n

for i in range(len(L)):
    L[i] = 0
    
i=0
j = 1
while(i < n):

    if((k % 2) == 0):        
        L[i] = 1        
        i = i + 2
    else:
        break

while(j < n):
    if((k % 2) == 1):        
        L[j] = 1        
        j = j + 2
    else:
        break
    
print(L, end="")

'''L = []
n = int(input("Enter number elements in List: "))
k = int(input("Enter a number: "))
print(n,"", k)
L = [None] * n

for i in range(len(L)):
    L[i] = 0
    
i=0
j = 1
while(i < n):

    if((k % 2) == 0):        
        L[i] = 1        
        i = i + 2
    else:
        break

while(j < n):
    if((k % 2) == 1):        
        L[j] = 1        
        j = j + 2
    else:
        break
    
for i in range(len(L)):
    print(L)
'''
