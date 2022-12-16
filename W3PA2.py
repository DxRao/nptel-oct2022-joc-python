#W3PA2


L = [3, 5, 7, 1, 10, 11, 22, 4, 67, 54, 2, 99]
n = 10
#L = []
#n


def rev(L, n):
    L.sort(reverse = True)
    #print(L)
    print(L[0:n], end = "") # prints index zero to n-1 (ie. 9) (Prints index 0 to index 9)

rev(L, n)
    
# Alternative, sort funtion:

    # sorted(L, reverse = True)

'''
#Write a function rev which takes a list L and integer n and print the
# first n largest numbers of the list.

#Input is managed for you, please write the required function only.

#Input:

#A list L and an integer n.

#Output:

#First n largest numbers

'''

