S = ""
S = input()
for i in range(len(S)):
    if (S[i] == 'a'):
        S = S.replace(S[i], "*")
    elif (S[i] == 'A'):
        S = S.replace(S[i], "*")
    elif (S[i] == 'e'):
        S = S.replace(S[i], "*")
    elif (S[i] == 'E'):
        S = S.replace(S[i], "*")
    elif (S[i] == 'i'):
        S = S.replace(S[i], "*")
    elif (S[i] == 'I'):
        S = S.replace(S[i], "*")
    elif (S[i] == 'o'):
        S = S.replace(S[i], "*")
    elif (S[i] == 'O'):
        S = S.replace(S[i], "*")
    elif (S[i] == 'u'):
        S = S.replace(S[i], "*")
    elif (S[i] == 'U'):
        S = S.replace(S[i], "*")            
    else:
        continue    
print(S, end = "")


'''
Write a program to take string S as an input and replace all vowels by *. Also print the modified string.

Input
A string S

Output
Modified string


Test Case 1	
The joy of computing
Th* j*y *f c*mp*t*ng

Test Case 2	
nptel
npt*l

Test Case 3	
python
pyth*n

Test Case 4	
swayam
sw*y*m
'''
