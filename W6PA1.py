#L = [11,3,2,2,1,4,1,13,7,5,15,9,7,7,4,7,7,8,9,0, 11,12, 13, 15]
#print(L)

L = []
L = [int(i) for i in input().split()]
d = {}

for i in L:
    if L.count(i) > 1:
        d[i] = [index for index, value in enumerate(L) if value == i]

print(d)


'''
lst = ['A', 'B', 'C', 'A', 'A', 'B']
from collections import defaultdict
pos_map = defaultdict(list)
for pos, ele in enumerate(lst):
     pos_map[ele].append(pos)

#pos_map

print(pos_map)
defaultdict(list, {'A': [0, 3, 4], 'B': [1, 5], 'C': [2]})

'''


'''
TrimedList = []
dictIndex = []
res = {}
res[50]= 0

for i in L:
    if(L.count(i) == 1):
        continue
    else:
        TrimedList.append(i)
        
#print(TrimedList)


index = 0
for value in TrimedList:
    print(value, end=' ')
    print(index, end = ' ')
    index += 1

'''

'''  
# using Dictionary comprehension + enumerate()
# Dictionary with index as value
res = {val : idx for idx, val in enumerate(TrimedList)}

print(res)




def Convert(a):    
    it = iter(a)
    res_dict = dict(zip(it, it))
    return res_dict
         
# Driver code

lst = [2, 2, 1, 4, 1, 5, 6, 5, 15, 6, 7, 7, 4, 7, 7, 15]

#print(Convert(lst))


Week 6: Programming Assignment 1

Due on 2022-09-08, 23:59 IST
Given a list L containing integers, write a program that creates and prints a dictionary 'd'
containing all the the numbers that occur twice or more in the list as keys and their indexes as values.
Both the keys are and their values should be in the same order as given the list.

You have to take the input.

Input
List

Output
Dictionary D


Input	Output
Test Case 1	
2 2 2 1 1 1
{2: [0, 1, 2], 1: [3, 4, 5]}
Test Case 2	
8 1 6 0 12 7 7 1 1 13 3 0 12 12 13 6 5 11 12 0
{1: [1, 7, 8], 6: [2, 15], 0: [3, 11, 19], 12: [4, 12, 13, 18], 7: [5, 6], 13: [9, 14]}
Test Case 3	
6 12 12 8 3 4 7 5 1 2 11 0 3 7 10 2 9 2 8 6
{6: [0, 19], 12: [1, 2], 8: [3, 18], 3: [4, 12], 7: [6, 13], 2: [9, 15, 17]}
Test Case 4	
0 12 3 8 10 12 4 1 5 4 4 11 9 2 0 8 1 8 9 11
{0: [0, 14], 12: [1, 5], 8: [3, 15, 17], 4: [6, 9, 10], 1: [7, 16], 11: [11, 19], 9: [12, 18]}


'''
