# [SIG Python Task 3] 

"""
TODO: 
a) Calculate the temperature altitude from a list of temperatures
b) Count frequency of every character in a string (using dictionaries)
c) Verify De Morgan Laws (using sets)

NOTE: Have Fun Coding!
"""


# a) Calculate the temperature altitude from a list of temperatures
"""
Given a list of temperatures of one day, calculate the temperature amplitude (difference between highest and lowest temperature). Keep in mind that sometimes there might be a sensor error (represented as 'error').
"""

from typing import Union


temperatures = [3, -20, -6, -12, 'error', 24, 18, 28, 16, 14]

# Write you code here


t = []

for i in temperatures:

    if i != 'error':
        t.append(i)                                                 #Removing errors from data

print ("Temperature Altitude = " , max(t) - min(t) , "\n\n\n")      #Calculating Altitude




# b) Count frequency of every character in a string (using dictionaries)
"""
Take a string as input from the user (for eg: 'abcccedeEEdffaG') and count the frequency each characters occurs in the string.

NOTE: Covert the string to upper or lower case first.
"""
# Write you code here



st = input("Enter String : ")
st = st.lower()                                                     #Coverting string to lowercase
D = {st[0] : 1 , }
P = D.keys()
Q = D.values()

for i in range (1,len(st) ):
    if st[i].isalpha():
        if st[i] not in P :
            D[ st[i] ] = 1

        else:
            D[ st[i] ] += 1

    P = D.keys()
    Q = D.values()

print ("Information:")
for i in P:
    print (i , ' : ' , D[i])

print ("\n\n")



# c) Verify De Morgan Laws (using sets)
"""
Given a Universal Set 'U', and two of its subsets 'A' and 'B'
Verify the De Morgan laws using sets. 

# De Morgan Laws:
not (A or B) = not A and not B
not (A and B) = not A or not B

NOTE: Use the inbuilt operators/methods for set operations (intersection, union, difference, ...)
NOTE: Complement of a set 'X' is the difference: 'U' - 'X'
"""

U = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
A = {0, 2, 4, 6, 8}
B = {3, 6, 9}

# Write your code here



X = U - (A.union(B))
Y = (U - A).intersection(U - B)

print ("U is " , U , "\nA is " , A , "\nB is " , B , "\n")

if X == Y:
    print ("Demorgan Law 1 : not (A or B) = not A and not B\nVERIFIED")

X = U - (A.intersection(B))
Y = (U - A).union(U - B)

if X == Y:
    print ("Demorgan Law 2 : not (A and B) = not A or not B\nVERIFIED\n")
    
# NOTE: Make sure to print few empty lines after each task