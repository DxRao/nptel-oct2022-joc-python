def replaceV(R):
    R=list(R)
    vowels = 'aeiou'
    returnString=""
    for i in range(0, len(R)):
        
        if R[i].lower() in vowels and R[i+1].lower() in vowels and R[i+2].lower() in vowels:
            returnString = returnString + '_'
            R[i] = '!'
            R[i+1] = '!'
            R[i+2] = '!'
        
        if R[i] != '!':
            returnString = returnString + R[i]
    return(returnString)

S = input()
print(replaceV(S))



'''
def replaceV(S):    
	vowels = 'AEIOUaeiou'
	k = '_'      
	for ele in vowels: 
		if S.count(ele) == 3:            
			S = S.replace(ele, k, 1) 
			S = S.replace(ele, '', 2)
		elif S.count(ele) > 3:
			S = S.replace(ele, ' ', 2) 
			S = S.replace(ele, k, 1)
	return S

'''

'''
def replaceV(w):
    w=list(w)
    v = 'aeiou'
    a=""
    for i in range(0, len(w)):
        try:
            if w[i].lower() in v and w[i+1].lower() in v and w[i+2].lower() in v:
                a = a + '_'
                w[i] = '*'
                w[i+1] = '*'
                w[i+2] = '*'
        except:
            pass
        if w[i] != '*':
            a = a + w[i]
    return(a)



S = input()
print(replaceV(S))
'''

'''
def replaceV(w):
    w=list(w)
    v = 'aeiou'
    a=""
    for i in range(0, len(w)):
        try:
            if w[i].lower() in v and w[i+1].lower() in v and w[i+2].lower() in v:
                a = a + '_'
                w[i] = '*'
                w[i+1] = '*'
                w[i+2] = '*'
        except:
            pass
        if w[i] != '*':
            a = a + w[i]
    return(a)



S = input()
print(replaceV(S))
'''

'''
#def replace_vowels(word):
word = input()
print(word)
k = "_"
m =""
n=""

vowels = ['a', 'e', 'i', 'o', 'u', 'A','E','I','O','U']
for x in range(len(word)):
    for x in range(len(vowels)):
        if word[x+1] in word:
            if vowels[x+1] in vowels:
                #if word[x+2] in word:
                    #if vowels[x+2] in vowels:
                        word = word.replace(word[x], k, 1)
                        word = word.replace(word[x+1], m, 1)
                        #word = word.replace(word[x+2], n, 1)
        print(word) 

#replace_vowels('Stackoverflow')

'''
'''
def replace_vowels(word):
        vowels = ['a', 'e', 'i', 'o', 'u']
        for x in (word.lower()):
                if x in vowels:
                        word = word.replace(x, "_")
        print(word) 

replace_vowels('Stackoverflow')



'''

'''
word = input("Enter a word: ")
new_word = ""
vowels = "aeiouy"

for letter in word:
    if letter in vowels:
        new_word += '_'
    else:
       new_word += letter

print(new_word)


'''
'''
#def replaceV(S):
    
word = str(input())
#word = ['s','d','a','a','a','w','e','e','e','r','i','i','i','k','m']
#word1 = input("Enter a word: ")
#word1 = str(word1)
#word = word1.split(',')




vowels = ['a','e','i','o','u','A','E','I','O','U']



k = "_"
m =''
n =''
for i in range(len(vowels)):
    for j in range(len(word)-1):    
        if  (vowels[i] == word[j+0])  and (vowels[i] == word[j+1]) and (vowels[i] ==  word[j+2]):
            if vowels[i] == word[j+0]:
                word = word.replace(word[j+0],k,1 )
                if vowels[i] == word[j+1]:
                    word = word.replace(word[j+1],m,1 )
                    if vowels[i] == word[j+2]:
                        word = word.replace(word[j+2],n,1)
        
        
print(word)

#print(replaceV(S))
'''

'''
# Function to Replace each vowel
# in the string with a specified character
def replaceVowelsWithK(test_str, K):
 
    # creating list of vowels
    vowels_list = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
 
    # creating empty list
    new_string = []
 
    # converting the given string to list
    string_list = list(test_str)
 
    # running 1st iteration for
    # comparing all the
    # characters of string with
    # the vowel characters
    for char in string_list:
 
        # running 2nd iteration for
        # comparing all the characters
        # of vowels with the string character
        for char2 in vowels_list:
 
            # comparing string character
            # and vowel character
            if char == char2:
 
                # if condition is true then adding
                # the specific character entered
                # by the user in the new list
                new_string.append(K)
                break
 
        # else adding the character
        else:
            new_string.append(char)
 
    # return the converted list into string
    return(''.join(new_string))
 
   
 
# Driver Code
# input string
input_str = "Geeks for Geeks"
 
# specified character
K = "#"
 
# printing input
print("Given String:", input_str)
print("Given Specified Character:", K)
 
# printing output
print("After replacing vowels with the specified character:",
      replaceVowelsWithK(input_str, K))
Output
Given String: Geeks for Geeks
Given Specified Character: #
After replacing vowels with the specified character: G##ks f#r G##k

'''


'''
def replaceV(S):    
    vowels = 'AEIOUaeiou'
    k = '_'      
    for ele in vowels: 
        if S.count(ele) == 3:            
            S = S.replace(ele, '', 2) 
            S = S.replace(ele, k, 1)
    return S

S = input()
print(replaceV(S))

'''

'''

def replaceVowelsWithK(test_str):
 
    # string of vowels
    vowels = 'AEIOUaeiou'
    k = '_'
    
    
 
    # iterating to check vowels in string
    for ele in vowels: 
        if test_str.count(ele) == 3:            
        # replacing vowel with the specified character
            
            test_str = test_str.replace(ele, '', 2) 
            test_str = test_str.replace(ele, k, 1)
        
        
 
    return test_str

test_str = input()
print(replaceVowelsWithK(test_str))
 
'''


'''
a=[]

b=str("a,a,a,b,e,e,e,c,x,d")

a=b.split(',')

c=['a','e','i','o','u','A','E','I','O','U']
j = 0
i=0
new_word = ""
for i in range(len(a) -2):
  if a[i] in c:
      if a[i] == a[i+1] == a[i+2]:
          del a[j]
          del a[j+1]
          del a[j+2]
          new_word += '_'
          
          
      else:
          new_word += a[j]          
          
  #j=0

print(a)

'''

'''

#def replaceV(S):
    

word = ['s','d','a','a','a','w','e','e','e','r','i','i','i','k','m']
#word1 = input("Enter a word: ")
#word1 = str(word1)
#word = word1.split(',')


print(word)
new_word = ""
vowels = ['a','e','i','o','u','A','E','I','O','U']

j = 0
for i in vowels:
    for j in range(len(word) - 3):
        if  i == word[j] and i == word[j+1] and i ==  word[j+2]:
            new_word += '_'
            j = j+3
        
        else:
            new_word += word[j]
        

print(new_word)

#S = input()
#print(replaceV(S))
'''




'''
Week 8: Programming Assignment 2
Due on 2022-09-22, 23:59 IST
Given a string S, write a function replaceV that accepts a string and replace the occurrences of 3 consecutive vowels
with _ in that string. Make sure to return the answer string.

Input:

aaahellooo

Output:

_hell_

Explanation:

Since aaa and ooo are consecutive 3 vowels therefor replaced by _ .



Input	Output
Test Case 1	
aaahellooo
        _hell_
Test Case 2	
happpyyyy Biiiirthdayyyyaaaa
        happpyyyy B_irthdayyyy_a
Test Case 3	
amanDeeepsiiingh
        amanD_ps_ngh
Test Case 4	
thiiis probleeem iiisss veeeery
        th_s probl_m _sss v_ery





'''
