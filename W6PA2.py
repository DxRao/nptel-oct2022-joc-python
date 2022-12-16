text = input()
def encrypt(text):
	result = ""   
	for i in range(len(text)):
		char = text[i]      
		if(char.isupper()):
			result += chr((ord(char) + (-3-65)) % 26 + 65)      
		elif char == ' ':
			result = result + ' '
		elif (char.isnumeric()):          
			result = result + char
		else:           
			result += chr((ord(char) + (-2-97)) % 26 + 97)
	return result

print(encrypt(text), end = '')


'''


text = input()
def encrypt(text):
    result = ""   
    for i in range(len(text)):
        char = text[i]
        if(char.isupper()):
            result += chr((ord(char) + (-3-65)) % 26 + 65)            
        elif char == ' ':
            result = result + ' '            
	elif(char.isnumeric()):            
	    result = result + char
	else:           
	    result += chr((ord(char) + (-2-97)) % 26 + 97)
    return result        

print(encrypt(text), end = '')
'''

'''
def encrypt(text):
    result = ""
   # transverse the plain text
    for i in range(len(text)):
        char = text[i]
      # Encrypt uppercase characters in plain text
      
        if(char.isupper()):
            result += chr((ord(char) + (-3-65)) % 26 + 65)
      # Encrypt lowercase characters in plain text
        elif char == ' ':
            result = result + ' '        
        else:           
            result += chr((ord(char) + (-2-97)) % 26 + 97)
    return result
#check the above function
text = "I Love You"
#s = -2

print("Plain Text : " + text)
#print("Shift pattern : " + str(s))
print("Cipher: " + encrypt(text))

'''

'''
def encrypt(text,s):
    result = ""
   # transverse the plain text
    for i in range(len(text)):
        char = text[i]
      # Encrypt uppercase characters in plain text
      
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
      # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result
#check the above function
text = "CEASER CIPHER DEMO"
s = -2

print("Plain Text : " + text)
print("Shift pattern : " + str(s))
print ("Cipher: " + encrypt(text,s))
'''


'''
Output
You can see the Caesar cipher, that is the output as shown in the following image −

Caesar cipher
Explanation
The plain text character is traversed one at a time.

For each character in the given plain text, transform the given character as per the rule
depending on the procedure of encryption and decryption of text.

After the steps is followed, a new string is generated which is referred as cipher text.

Hacking of Caesar Cipher Algorithm
The cipher text can be hacked with various possibilities. One of such possibility is Brute Force Technique,
which involves trying every possible decryption key. This technique does not demand much effort and is relatively simple for a hacker.

The program implementation for hacking Caesar cipher algorithm is as follows −

message = 'GIEWIVrGMTLIVrHIQS' #encrypted message
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(LETTERS)):
   translated = ''
   for symbol in message:
      if symbol in LETTERS:
         num = LETTERS.find(symbol)
         num = num - key
         if num < 0:
            num = num + len(LETTERS)
         translated = translated + LETTERS[num]
      else:
         translated = translated + symbol
print('Hacking key #%s: %s' % (key, translated))

'''


'''
import string

s = "i love you"
l =[]
dict = {}
for i in range(s):    
        l.append(string.ascii_letters[i - 2])
    #else:
        #dict[string.ascii_letters[i]] = string.ascii_letters[i - 3]

print(dict, end = '')

'''


'''

Week 6: Programming Assignment 2
Due on 2022-09-08, 23:40 IST
Romeo and Juliet love each other. Romeo wants to send a message to Juliet and also don't want anyone
to read it without his permission. So he shifted every small letter in the sentence by -2 position and
every capital letter by -3 position. (If the letter is c, after shifting to by -2 position it changes to a, and for D new letter will be A).
But the letter is too long and Romeo does not have enough time to encrypt his whole letter.
Write a program to help Romeo which prints the encrypted message. You can assume there are
no special characters except spaces and numeric value.

Input
A string S 

Output 
Encrypted string 

Example

Input
Hello Juliet

Output
Ecjjm Gsjgcr

Explanation
H is shifted by -3 position and changed to E. 'e' is shifted by -2 position and changed to c and so on.



	Input	Output
Test Case 1	
Hello Juliet
                Ecjjm Gsjgcr
Test Case 2	
Lets meet tonight
                Icrq kccr rmlgefr
Test Case 3	
How are you
                Emu ypc wms
Test Case 4	
When will you return
                Tfcl ugjj wms pcrspl

'''
