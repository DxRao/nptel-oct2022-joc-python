string = input()
substring = input()
print(substring in string)



'''
Week 9: Programming Assignment 1
Due on 2022-09-29, 23:59 IST
Given two strings s1 and s2, write a function subStr that accepts two strings s1 and s2 and will return True if a s2 is a substring of s1 otherwise return False. A substring is a is a contiguous sequence of characters within a string. 

Input:

bananamania
nana

Output:
True

Explanation:

S2 which is nana is in bananamania hence it is a substring of s1.

Example 2:

Input:

aabbcc
abc

output:
False

Explanation:

String s1 does not contain string s2 hence the answer is false.''



Input	Output
Test Case 1	
bananamania
nana
        True
Test Case 2	
aaabbbccc
aaa
        True
Test Case 3	
aaaaaaaaaa
aa
        True
Test Case 4	
aabbcc
abc
        False


'''
