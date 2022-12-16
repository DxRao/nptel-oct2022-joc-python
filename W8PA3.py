L = list(map(int, input().split()))

for i in L:
    if i == 0:
        L.remove(i)
        L.append(0)
        
print(L)



'''
Week 8: Programming Assignment 3
Due on 2022-09-22, 23:59 IST
Given a list L, write a program to shift all zeroes in list L towards the right
by maintaining the order of the list. Also print the new list.

Input:

[0,1,0,3,12]

Output:

[1,3,12,0,0]

Explanation:

There are two zeroes in the list which are shifted to the right and the order of the list
is also maintained. (1,3,12 are in order as in the old list.)



nput	Output
Test Case 1	
5 1 0 6 7 8 10 9 0 2 
        [5, 1, 6, 7, 8, 10, 9, 2, 0, 0]
Test Case 2	
6 3 2 4 9 1 0 1 7 3 6 0 10 5 10 
        [6, 3, 2, 4, 9, 1, 1, 7, 3, 6, 10, 5, 10, 0, 0]
Test Case 3	
8 11 15 17 19 20 6 6 8 11 5 15 18 3 9 
        [8, 11, 15, 17, 19, 20, 6, 6, 8, 11, 5, 15, 18, 3, 9]
Test Case 4	
0 0 0 0 3 
        [3, 0, 0, 0, 0]


'''
