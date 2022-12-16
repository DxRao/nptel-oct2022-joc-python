def closestSchool(x, y, L):
  min=99999
  distance=[]
  for i in L: 
    dis=((x-i[0])**2+(y-i[1])**2)**0.5
    distance.append(dis)
    if dis<min:
      min=dis 
  for i in range(len(distance)):
    if distance[i]==min:
        print(L[i])

L = []
L = [int(i) for i in input().split()]
closestSchool(2, 5, L)






#~~~THERE IS SOME INVISIBLE CODE HERE~~~
        
'''
Week 10: Programming Assignment 2
Due on 2022-10-06, 23:59 IST

Ram shifted to a new place recently. There are multiple schools near his locality.
Given the co-ordinates of Ram P(X,Y) and schools near his locality are given in a nested list,
find the closest school. Print multiple coordinates in respective order if there exist multiple
schools closest to him. Write a function closestSchool that accepts (X ,Y , L) where X and Y
are co-ordinates of Ram's house and L contains co-ordinates of different school.

Distance Formula(To calculate distance between two co-ordinates): √((X2 - X1)² + (Y2 - Y1)²)

where (x1,y1) is the co-ordinate of point 1 and (x2, y2) is the co-ordinate of point 2.

Input:
X, Y (Ram's house co-ordinates)
N (No of schools)
X1 Y1
X2 Y2
.
.
.

X6 Y6

Output:
Closest point/points to X, Y

	Input	Output

Test Case 1	
1 1
5
3 0
0 0
5 -9
-6 2
-4 -5
                [0, 0]
Test Case 2	
0 0
3
-3 9
-8 3
7 -5
                [-8, 3]
Test Case 3	
-2 0
3
-9 -6
-5 6
6 -1
                [-5, 6]
Test Case 4	
-1 -2
4
6 -4
6 -4
8 0
-8 -10
                [6, -4]
                [6, -4]




////////////////////////////////////////////////////////////////////////////////////////////
Ram shifted to a new place recently. There are multiple schools near his locality.
Given the co-ordinates of Ram P(X,Y) and schools near his locality in a nested list,
find the closest school. Print multiple coordinates in respective order if there exists
multiple schools closest to him. Write a function closestSchool that accepts (X ,Y , L)
where X and Y are co-ordinates of Ram’s house and L contains co-ordinates of different school.
/////////////////////////////////////////////////////////////////////////////////////////////////

'''

'''
def closestSchool(x, y, L):
  min=99999
  distance=[]
  for i in L: 
    dis=((x-i[0])**2+(y-i[1])**2)**0.5
    distance.append(dis)
    if dis<min:
      min=dis 
  for i in range(len(distance)):
    if distance[i]==min:
        print(L[i])

L = []
L = [int(i) for i in input().split()]
closestSchool(2, 5, L)

'''
