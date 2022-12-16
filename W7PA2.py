n = int(input())
M = []
for i in range(n):
    L = list(map(int, input().split()))
    M.append(L)

def Transpose(m):
    T = list()
    a = 0
    
    for column in m:
        column1 = []
        for column in m:        
            column1.append(column[a])       
        T.append(column1)
        a = a + 1   
    
    return (T)
   
print(Transpose(M))


'''
n = int(input())
M = []
for i in range(n):
    L = list(map(int, input().split()))
    M.append(L)

def Transpose(m):
    T = list()
    for i in range(len(m[0])):
        column = []
        for j in range(len(m)):        
            column.append(m[j][i])       
        T.append(column)
    return (T)   
    
print(Transpose(M))
'''


'''
Week 7: Programming Assignment 2
Due on 2022-09-15, 23:59 IST
Given a matrix M write a function Transpose which accepts a matrix M and return the transpose of M.
Transpose of a matrix is a matrix in which each row is changed to a column or vice versa.

Input 
A matrix M
[[1,2,3],[4,5,6],[7,8,9]]

Output
Transpose of M
[[1,4,7],[2,5,8],[3,6,9]]

Explanation:

Matrix M was
1
1 2 3 
2
4 5 6 
3
7 8 9 


After changing all rows into columns or vice versa M will become
1
1 4 7 
2
2 5 8 
3
3 6 9



Input	             Output
Test Case 1	
3
51 81 52 
100 18 2 
90 59 58 
                    [[51, 100, 90], [81, 18, 59], [52, 2, 58]]
Test Case 2	
4
20 41 90 85 
58 90 16 91 
10 11 18 87 
41 67 94 6 
                    [[20, 58, 10, 41], [41, 90, 11, 67], [90, 16, 18, 94], [85, 91, 87, 6]]
Test Case 3	
2
10 89 
99 74 
                    [[10, 99], [89, 74]]
Test Case 4	
3
9 23 5 
63 48 40 
48 23 42 
                    [[9, 63, 48], [23, 48, 23], [5, 40, 42]]



'''
