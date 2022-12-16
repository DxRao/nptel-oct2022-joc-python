def count_letters(S):
    freq_dict = {}
    for item in S:
        if (item in freq_dict):
            freq_dict[item] = freq_dict[item] + 1
        else:
            freq_dict[item] = 1
    #print(freq_dict, end='')
    return freq_dict
           
                 

    
if __name__ == "__main__":
    S = input()
    d = count_letters(S)
    print(d, end='')



'''

def count_letters(S):
    freq_dict = {}
    for item in S:
        if (item in freq_dict):
            freq_dict[item] = freq_dict[item] + 1
        else:
            freq_dict[item] = 1
    print(freq_dict, end='')
    return freq_dict                

    
if __name__ == "__main__":
    S = input()
    d = count_letters(S)

'''

'''

def count_letters(S):
    freq = {}
    for item in S:
        if (item in freq):
            freq[item] = freq[item] + 1
        else:
            freq[item] = 1
    for key, value in freq.items():
        print("'%c': %d, "%(key,value), end = '')

print(freq_dict, end='')
                 


if __name__ == "__main__":
    S = input()
    d = count_letters(S)
'''




'''

Week 5: Programming Assignment 1
Due on 2022-09-01, 23:59 IST
You are given a string S. Write a function count_letters which accepts the string S and
returns a dictionary containing letters (including special character) in string S as keys and their count in string S as values.

(input and output is handled by us, you just need to write the function and return the dictionary)

Input
The Joy of computing

Output
{'T': 1, 'h': 1, 'e': 1, ' ': 3, 'j': 1, 'o': 3, 'y': 1, 'f': 1, 'c': 1, 'm': 1, 'p': 1, 'u': 1, 't': 1, 'i': 1, 'n': 1, 'g': 1}

Explanation: T is appeared once in the string, similarly o is appeared 3 times in the string and so on.
(You do not have to worry about the order of arrangement in your dictionary)
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@





if __name__ == "__main__":
    S = input()
    d = count_letters(S)
~~~THERE IS SOME INVISIBLE CODE HERE~~~
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

	Input	Output
Test Case 1	
The joy of computing
{'T': 1, 'h': 1, 'e': 1, ' ': 3, 'j': 1, 'o': 3, 'y': 1, 'f': 1, 'c': 1, 'm': 1, 'p': 1, 'u': 1, 't': 1, 'i': 1, 'n': 1, 'g': 1}
Test Case 2	
Nptel!!!
{'N': 1, 'p': 1, 't': 1, 'e': 1, 'l': 1, '!': 3}
Test Case 3	
Made in India!
{'M': 1, 'a': 2, 'd': 2, 'e': 1, ' ': 2, 'i': 2, 'n': 2, 'I': 1, '!': 1}
Test Case 4	
Hello World
{'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'W': 1, 'r': 1, 'd': 1}




'''
