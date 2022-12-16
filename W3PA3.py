# W3PA3

L = [int(i) for i in input().split()]
count1 = 0
for z in range(len(L)):
    if((L[z] % 2) == 1):
        count1 = count1 + 1
    else:
        continue
print(count1, end = "")


#Write a program to count and print the number of odd numbers in a list L.

#Input is managed for you.

#Input:
#A list L

#Output:
#Total number of odd numbers.


