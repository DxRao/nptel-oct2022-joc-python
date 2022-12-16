n = int(input())

S = str(n)
my_dict = {}


for i, n in enumerate(str(S)):   
    if str(S).count(n) == 1:
        if int(S[i]) not in my_dict:
            my_dict[int(S[i])] = [i]
        else:
            my_dict[int(S[i])].append(i)        
    else:       
        if str(S).count(n) > 1:
            if int(S[i]) not in my_dict:
                my_dict[int(S[i])] = [i]
            else:                
                my_dict[int(S[i])].append(i)
            
for x in my_dict:
    print(x, *my_dict[x],"")
            

'''
n = int(input())
S = str(n)
my_dict = {}

for i in range(len(S)):
    if int(S[i]) not in my_dict:
        my_dict[int(S[i])] = [i]
    else:
        my_dict[int(S[i])].append(i)
        
for x in my_dict:
    print(x, *my_dict[x], "")

'''


        
'''
# using dict()
my_dict = dict({1:'apple', 2:'ball'})

# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])

'''

'''
Week 9: Programming Assignment 3
Due on 2022-09-29, 23:59 IST
Given an integer n, print all the indexes of numbers in that integer from left to right.

Input:
122345

Output:
1 0 
2 1 2
3 3
4 4
5 5

Explanation:

Given integer 122345. Now printing indexes of numbers from left to right.
The First number is 1 and its index is 0 therefore
1 0 


The second and the third number is 2 and its index is 1,2 therefore
2 1 2

and so on...


Input	Output
Test Case 1	
122345
1 0 
2 1 2 
3 3 
4 4 
5 5
Test Case 2	
123456789
1 0 
2 1 
3 2 
4 3 
5 4 
6 5 
7 6 
8 7 
9 8 
Test Case 3	
89832913
8 0 2 
9 1 5 
3 3 7 
2 4 
1 6 
Test Case 4	
7856691
7 0 
8 1 
5 2 
6 3 4 
9 5 
1 6 


'''
