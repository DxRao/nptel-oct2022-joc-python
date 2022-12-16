#~~~THERE IS SOME INVISIBLE CODE HERE~~~
L =[]

L = [int(i) for i in input().split()]

z=sorted(list(set(L)))
a=[0]*(max(z)+1)
for i in range(len(z)):
  a[z[i]]=z[i]
print(*a,end="")


'''
Week 10: Programming Assignment 1
Due on 2022-10-06, 23:59 IST
Given a list L, write a program to make a new list to fix the indexes of numbers in the list L to its same value in the new list.
Put 0 at remaining indexes.
Also print the elements of the new list in the single line. (See explanation for more clarity.)

Input:
[1,5,6]

Output:
0 1 0 0 0 5 6

Explanation: 

List L contains 1,5,9 so at 1,5,9, index of new list the respective values are put and rest are initialized as zero.

Input	Output
Test Case 1	
1 5 9
        0 1 0 0 0 5 0 0 0 9
Test Case 2	
2 8 8 6 8
        0 0 2 0 0 0 6 0 8
Test Case 3	
1 0 6 1 5
        0 1 0 0 0 5 6
Test Case 4	
1 4 1 2 3
        0 1 2 3 4


/////////////////////////////

Given a list L write a program to make a new list to fix the indexes of numbers
to in list L to its same value in the new list. Put 0 at remaining indexes. Also print the elements
of the new list in the single line. (See explanation for more clarity.)

'''

'''
#~~~THERE IS SOME INVISIBLE CODE HERE~~~
L =[]

L = [int(i) for i in input().split()]

SL=sorted(list(set(L)))
IL=[0]*(max(SL)+1)
for i in range(len(SL)):
  IL[SL[i]]=SL[i]
print(*IL,end="")
'''
