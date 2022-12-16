n = int(input())
M = []
for i in range(n):
    L = list(map(int, input().split()))
    M.append(L)

print(snake(M))



'''
def snake(a):
    m = n
    p = n
    k =0
    l =0
    L = []
    while(k<m):    
        for i in range(l, p):
            L.append(a[k][i])        
    
        k = k + 1
        if k == m:
            break
        for j in range(p-1, -1, -1):           
            L.append(a[k][j])       
        
        k = k + 1        
    return L

n = int(input())
M = []
for i in range(n):
    L = list(map(int, input().split()))
    M.append(L)

print(snake(M))

'''

'''
def snake(m):
    while( n >= 0):
        L = []
        for i in range(A): 
            if i % 2 == 0:
                for j in range(B):
                    L.append(m[i][j])
                #print(str(m[i][j]), end=" ")        
            else:
                for j in range(B - 1, -1, -1):
                    L.append(m[i][j])
                #print(str(m[i][j]), end=" ")
        return L
    return -1
 
 
n = int(input())
A = n
B = n
M = []
for i in range(n):
    L = list(map(int, input().split()))
    M.append(L)

print(snake(M))

'''

'''
def snake(m):
    while( n >= 0):
        L = []
        for i in range(A): 
            if i % 2 == 0:
                for j in range(B):
                    L.append(m[i][j])
                #print(str(m[i][j]), end=" ")        
            else:
                for j in range(B - 1, -1, -1):
                    L.append(m[i][j])
                #print(str(m[i][j]), end=" ")
        return L
    return -1
 
 
n = int(input())
A = n
B = n
M = []
for i in range(n):
    L = list(map(int, input().split()))
    M.append(L)

print(snake(M))

'''


'''
def snake(m):
    result = []
    a = 0
    b = -1
    c = 0
    for i in m:
        for j in m:
            result.append(i[a])
            a = a + 1
            for j in m:
                result.append(j[b])
                b = b - 1           
                print(result)

n = int(input())
M = []
for i in range(n):
    L = list(map(int, input().split()))
    M.append(L)

print(snake(M))

'''

'''
Week 7: Programming Assignment 3
Due on 2022-09-15, 23:59 IST
Given a matrix M write a function snake that accepts a matrix M and returns a list which contain
elements in snake pattern of matrix M. (See explanation to know what is snake pattern)

Input
A matrix M
91 59 21 63 
81 39 56 8 
28 43 61 58 
51 82 45 57

Output
[91, 59, 21, 63, 8, 56, 39, 81, 28, 43, 61, 58, 51, 82, 45, 57]

Explanation:

For row 1 elements are inserted from left to right
For row 2 elements are inserted from right to left
For row 3 elements are inserted form left to right 
and so on



Input	Output
Test Case 1	
4
44 80 90 37 
96 75 57 20 
31 99 94 36 
74 49 57 81 

                [44, 80, 90, 37, 20, 57, 75, 96, 31, 99, 94, 36, 81, 57, 49, 74]
Test Case 2	
3
67 4 93 
2 50 76 
51 73 64 
                [67, 4, 93, 76, 50, 2, 51, 73, 64]
Test Case 3	
2
91 58 
92 7 
                [91, 58, 7, 92]
Test Case 4	
1
82 
                [82]

'''
