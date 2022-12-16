def UniqueE(L):    
    UniqueList = []
    for item in L:
        if item in UniqueList:
            continue            
        else:
            if L.count(item) < 2:
                UniqueList.append(item)
                UniqueList.sort()
    return UniqueList

L = [99,1,2,3,3,4,4,2,5,5,6,7,8,8,8,10,11,11,11,11,13,67,45,99]

print(UniqueE(L), end ='')




'''
def get_unique_numbers(numbers):
    unique = []

    for number in numbers:
        if number in unique:
            continue
        else:
            unique.append(number)
    return unique


print(get_unique_numbers(numbers))
# Result: [20, 30, 40]
'''


'''
def UniqueE(L):    
    UniqueList = []
    for item in L:
        if item in UniqueList:
            continue            
        else:
            if L.count(item) < 2:
                UniqueList.append(item)
                UniqueList.sort()
    return UniqueList

L = [99,1,2,3,3,4,4,2,5,5,6,7,8,8,8,10,11,11,11,11,13,67,45,99]

print(UniqueE(L), end ='')


'''



'''
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

'''

L = [99,1,2,3,3,4,4,2,5,5,6,7]

UniqueList = []

def UniqueE(L):
    for i in L:
        #temp = i
        #print(temp)
        for j in range(1, len(L)):
            #next = j
            #print(next)
            if(i != j):
                #break
                continue               
                #temp = next
                #next = j+1            
    UniqueList.append(i)
   

UniqueE(L)
UniqueList.sort()
print(UniqueList, end='')

'''

'''
Week 5: Programming Assignment 2
Due on 2022-09-01, 23:59 IST
You are given a list L. Write a function uniqueE which will return a list of unique elements is the list L in sorted order.
(Unique element means it should appear in list L only once.)

Input is handled by us.

Input
[1,2,3,3,4,4,2,5,6,7]

Output
[1,5,6,7]

Explanation

Elements 1,5,6,7 appears in the input list only once.
@@@@@@@@@@@@@@@@@@




L = [int(i) for i in input().split()]
print(uniqueE(L))


@@@@@@@@@@@@@@@@@@@@@@@@@@

Input	Output
Test Case 1	
4 12 11 1 14 10 7 2 12 3
[1, 2, 3, 4, 7, 10, 11, 14]
Test Case 2	
13 8 7 13 10
[7, 8, 10]
Test Case 3	
1 2 1 11 7 2 10
[7, 10, 11]
Test Case 4	
3 9 10 14 14 4 2
[2, 3, 4, 9, 10]

'''
