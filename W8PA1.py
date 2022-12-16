def cubeT(L):
    tupleL = []
    for val in L:
        tupleL.append(val*val*val)
    tuple1 = tuple(tupleL)
    return str(tuple1)


L = [int(i) for i in input().split()]
print(cubeT(L))


'''

Week 8: Programming Assignment 1
Due on 2022-09-22, 23:59 IST
Write a function cubeT that accepts a list L and returns a tuple containing cubes of elements of L.

Input
A tuple T

Output 
Cube of T


nput	Output
Test Case 1	
2 7 5 5 4 10 5 9 1 10
        (8, 343, 125, 125, 64, 1000, 125, 729, 1, 1000)
Test Case 2	
1 1 2 5 5 5 7 7 2 5
        (1, 1, 8, 125, 125, 125, 343, 343, 8, 125)
Test Case 3	
47 33 61 69 83 51 97 57 58 93
        (103823, 35937, 226981, 328509, 571787, 132651, 912673, 185193, 195112, 804357)
Test Case 4	
6 4 19 19 20 18 19 17 10 10
        (216, 64, 6859, 6859, 8000, 5832, 6859, 4913, 1000, 1000)
        
'''
