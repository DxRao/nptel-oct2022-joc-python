n = int(input())
M = []
for i in range(n):
    L = list(map(int, input().split()))
    M.append(L)

def DiagCalc(m):
    column1 = []
    column2 = []
    a = 0
    b = 1
    c = -1
    d = -2
    for row in m:
        column1.append(row[a])
        column2.append(row[c])
        a = b
        b = b + 1
        c = d
        d = d - 1
    Sum1 = sum(column1)
    Sum2 = sum(column2)
    print(Sum1)
    print(Sum2)

DiagCalc(M)


'''
Week 7: Programming Assignment 1
Due on 2022-09-15, 23:59 IST
Given a sqaure matrix M, write a function DiagCalc which calculate the sum of left and right diagonals
and print it respectively.(input will be handled by us)

Input:

A matrix M 
[[1,2,3],[3,4,5],[6,7,8]] 

Output 
13
13

Explanation:
Sum of left diagonal is 1+4+8 = 13
Sum of right diagonal is 3+4+6 = 13




Input	Output
Test Case 1	
3
18 81 60 
97 91 99 
90 54 21
                130
                241
Test Case 2	
4
43 73 70 78 
77 46 22 95 
32 22 47 5 
35 83 95 61 
                197
                157
Test Case 3	
4
69 80 34 4 
90 70 76 16 
78 25 6 48 
7 64 9 70 
                215
                112
Test Case 4	
20
72 6 40 67 47 83 23 45 14 44 7 15 96 49 59 20 29 37 52 37 
18 68 34 44 52 67 45 91 62 22 32 39 10 42 87 36 99 4 67 56 
53 66 89 72 27 15 80 87 86 89 20 97 22 13 76 66 15 65 87 38 
69 61 86 18 84 38 50 92 99 52 32 98 10 5 57 8 60 48 84 92 
80 33 71 90 20 15 90 29 9 48 98 90 58 19 50 43 44 76 53 67 
90 1 26 90 89 6 49 26 92 98 80 61 50 20 57 44 88 66 33 35 
58 42 96 95 33 37 89 41 41 35 34 18 16 11 28 6 31 64 37 87 
44 6 31 92 13 71 76 67 18 35 96 100 64 17 98 61 71 23 25 63 
9 91 30 57 1 82 38 5 21 23 97 39 57 31 25 6 24 74 40 49 
7 83 65 54 89 74 50 67 99 1 61 90 76 43 77 6 35 23 26 50 
76 79 91 9 6 81 34 53 89 76 76 93 61 97 68 13 7 64 98 92 
15 60 55 15 56 86 56 75 37 48 91 16 9 35 73 53 92 33 99 45 
75 94 79 59 17 92 92 96 11 83 23 63 41 44 17 4 44 18 68 86 
29 97 100 31 33 64 81 71 57 36 11 69 50 70 30 38 90 42 83 36 
65 78 24 35 53 53 83 100 9 26 95 60 53 2 63 29 91 91 42 89 
52 54 67 34 15 1 69 26 66 46 6 39 29 49 84 47 23 44 86 76 
7 41 54 37 80 31 89 31 36 99 68 85 49 75 78 56 25 62 32 34 
59 99 17 96 24 15 13 32 27 40 71 17 57 60 9 27 42 52 63 7 
14 59 82 18 37 85 11 76 73 62 36 75 13 90 34 57 52 31 75 70 
96 84 97 14 51 53 22 12 35 77 46 99 76 40 72 65 45 99 47 87 
                                                                1003
                                                                1071


'''
