#W3PA1

L = [int(i) for i in input().split()]
#L = [1,8,5,7,10,15,60,50,77,21,28,14,99,90,49]
P = []
for a in range(len(L)):
    if((L[a] % 5) == 0 or (L[a] % 7) == 0):
        P.append(L[a])
    else:
        continue
P.sort()
print(P)



'''
Week 3: Programming Assignment 1
Due on 2022-08-18, 23:59 IST
There is list L containing some numbers. Write a program to create a new list
which contains the numbers which are either divisible by 5 or 7 or both.
Print that new list in ascending order.

Input is already managed for you.

Input:
A list L
Output: A new list P

Example
Input:
L = [7, 8, 9, 10, 11]

Output:
[7, 10]'


'''
