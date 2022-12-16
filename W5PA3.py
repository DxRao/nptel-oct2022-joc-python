L = [1,14,16,10,4,6,3,12,6,20,9,11]
for i in L:
    counter = 0
    for j in range(1, i):
        if (i%j) == 0:
            counter = counter + 1
    if(counter == 1):
        print(i, end='')
        break    


'''

# Print all prime numbers in a list

#L = [1,4,12,6,34,56,11,2,5,7]

L = [int(i) for i in input().split()]
prime = []
for i in L:
    counter = 0
    for j in range(1, i):
        if i%j == 0:
            counter = counter + 1
    if counter == 1:
        prime.append(i)
print(prime, end=' ')

'''

'''
# Alternatively, Print first prime number in a given list by appending to a list
L = [int(i) for i in input().split()]
prime = []
for i in L:
    counter = 0
    for j in range(1, i):
        if i%j == 0:
            counter = counter + 1
    if counter == 1:
        prime.append(i)
print(prime[0])
'''


'''
L = [int(i) for i in input().split()]
prime = []
for i in L:
    counter = 0
    for j in range(1, i):
        if i%j == 0:
            counter = counter + 1
    if counter == 1:
        prime.append(i)
print(prime[0])


'''



'''

Week 5: Programming Assignment 3
Due on 2022-09-01, 23:59 IST
You are given a list L. Write a program to print first prime number encountered in the list L.(Treat numbers below and equal to 1 as non prime)

Input is handled by us.

Input
[1,2,3,4,5,6,7,8,9]

output
2

Explanation
Since 2 is the first prime number is list L, therefor it is printed.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
~~~THERE IS SOME INVISIBLE CODE HERE~~~


@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Sample:
input	Output
Test Case 1	
1 2 3 4 5 6 7 8 9
2
Test Case 2	
3 4 7 2 5 1 7 3 4 3
3
Test Case 3	
18 7 16 3 13 11 12 17 9 9
7
Test Case 4	
7 9 2 15 10 14 1 8 3 10
7

'''
