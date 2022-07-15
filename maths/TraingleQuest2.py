#Approach 1 - Math functions
from math import floor
for i in range(1,int(input())+1): print (pow(floor((pow(10,i)-1)/9),2))

#Approach 2 - Math operators
for i in range(1,int(input())+1):
    print (((10**i - 1)//9)**2)