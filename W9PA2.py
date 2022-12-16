def mergeDic(dict1,dict2):    
    dict3 = dict1.copy()
    dict3.update(dict2)
    dict3.update(dict1)
    return dict3

key = list(map(int, input().split()))
val = list(map(int, input().split()))

d1 = {}
for i in range(len(key)):
    d1[key[i]] = val[i]
    
d2 = {}
key = list(map(int, input().split()))
val = list(map(int, input().split()))
for i in range(len(key)):
    d2[key[i]] = val[i]

print(mergeDic(d1,d2))



'''

def mergeDic(a1, a2):
    md = {}
    
    for i in range(len(a1)):
        if i in a1[key[i]] != a2[key[i]]:
            md = {**a1, **a2}
        else:
            continue       
    return md

print(d1)
print(d2)

print(mergeDic(d1, d2))
'''

'''
Week 9: Programming Assignment 2
Due on 2022-09-29, 23:59 IST
Given two dictionaries d1 and d2, write a function mergeDic that accepts two dictionaries d1 and d2 and
return a new dictionary by merging d1 and d2. 
Note: Contents of d1 should be appear before contents of d2 in the new dictionary and in same order.
In case of duplicate value retain the value present in d1.

Input:
{1: 1, 2: 2}
{3: 3, 4: 4}

output:
{1: 1, 2: 2, 3: 3, 4: 4}


Input	Output
Test Case 1	
5 10 6 8 3 4 
61 95 72 22 14 22 
9 10 6 
25 20 93
        {5: 61, 10: 95, 6: 72, 8: 22, 3: 14, 4: 22, 9: 25}
Test Case 2	
0 7 5 
12 19 88 
5 0 
16 27
        {0: 12, 7: 19, 5: 88}
Test Case 3	
6 10 8 
54 45 86 
12 14 11 
98 50 13 
        {6: 54, 10: 45, 8: 86, 12: 98, 14: 50, 11: 13}
Test Case 4	
5 0 7 
90 51 17 
19 6 3 16 
44 78 68 70 
        {5: 90, 0: 51, 7: 17, 19: 44, 6: 78, 3: 68, 16: 70}


'''
