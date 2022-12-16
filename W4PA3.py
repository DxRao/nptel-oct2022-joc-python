N = 0
N = int(input())

for i in range(0, N):
    for j in range(0, i + 1):
        print("*", end = ' ')
    print("\r")

for i in range(N, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")

'''
Write a program to take an integer N as an input and display the pattern.

Input
5

Output
1
*
2
* *
3
* * *
4
* * * *
5
* * * * *
6
* * * *
7
* * *
8
* *
9
*

@@@@@@@@@@@@@@@@@@@@@@@
Test Case 1	
5
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
Test Case 2	
7
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * * * 
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
*
Test Case 3	
1
* 
Test Case 4	
4
* 
* * 
* * * 
* * * * 
* * * 
* * 
* 

'''





