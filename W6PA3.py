S = input().lower()
if(list(S) == list(S)[::-1]):
    print("palindrome", end = '')
else:
    print("not palindrome", end = '')



'''

import string
s = input()
def isPalindrome(s):
    return s == s[::-1]
ans = ""
if (len(s) != None):
    ans = isPalindrome(s)    
 
if ans:
    print("palindrome")
elif len(s) == None:
    print("palindrome", end = '')
else:
    print("not palindrome")
'''

'''
s = ""
s = input("Please input a String: ")


def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

 
print("The original string is : ", end="")
print(s)
 
c = reverse(s)
print("Reversed string is: ", c)

if c == s:
    print("palindrome", end = '')
else:
    print("not palindrome", end = "")
'''



'''
Week 6: Programming Assignment 3
Due on 2022-09-08, 23:59 IST
Take a string S as an input and print 'palindrome' if string S is a palindrome or 'not palindrome' if string S is not a palindrome.
A palindrome is a word which spells same from forward and backward. Example DAD.

Input

A string S

Output:

palindrome or not palindrome

Input	Output
Test Case 1	
DAD
            palindrome
Test Case 2	
kayak

            palindrome
Test Case 3	
joy
            not palindrome
Test Case 4	
computers
            not palindrome
'''
