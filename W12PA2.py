# Given a list of strings, sort the list of strings
# on the basis of last character andthe ones' before that of each string within the output.

L = input().split()
X=[]
for i in L:
  X.append("".join(list(i)[::-1]))
Y=[]  
for i in sorted(X):
  Y.append("".join(list(i)[::-1]))
print(Y, end='')



'''
Week 12: Programming Assignment 2
Due on 2022-10-20, 23:59 IST
Take a list of strings as an input and write a program to write sort the list of strings on the basis of last character of each string.
If last character is same, consider the second last character and so on.

Input:
L = ['ram', 'shyam', 'lakshami']

Output:
['lakshami', 'ram', 'shyam']

'''



'''
# Different program of past Week-12 prog assignment.

n=[]
for i in(input().split()):
  n.append(int(i))
n.sort()
print(n[-1]+n[-2],end='')

'''

