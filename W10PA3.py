
s= input()
myString = ""

for i in range (len(s)):
    if s[i] == s[i].lower():
        myString =  myString + s[i].upper()
    elif s[i] == s[i].upper():
        myString = myString + s[i].lower()
        
        
        #myString[i] = myString[S[i]] + S[val].swapcase()
print(myString, end='')
        







#print(input().swapcase(), end="")



'''
Week 10: Programming Assignment 3
Due on 2022-10-06, 23:59 IST
Given a string s write a program to convert uppercase letters into lowercase and
lowercase letters into uppercase. Also print the resultant string.

Note: You need to take the input and do not print anything while taking input.

Input:
The Joy Of Computing

Output
tHE jOY oF cOMPUTING

Input	Output
Test Case 1	
The Joy Of Computing
        tHE jOY oF cOMPUTING
Test Case 2	
hello 
        HELLO
Test Case 3	
YeaH
        yEAh
Test Case 4	
Python 3.0
        pYTHON 3.0


Given a string s write a program to convert uppercase letters into
lowercase and lowercase letters into uppercase. Also print the resultant string.

'''
