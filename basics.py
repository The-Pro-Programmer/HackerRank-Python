#Print
print("Hello, World!")

#Arithmatic
#Adding number - int() provides type conversion of string to integer
#a = int(input('Enter number a: '))
#b = int(input('Enter number b: '))
#print('Addition is: ', (a+b))

#Adding / concat string
#a = input('Enter number a: ')
#b = input('Enter number b: ')
#print('Addition is: ', (a+b))

print("Python data types:")
print("Numeric (immutable): Integer, Float, Complex")

#Numerics
#Numeric immutability - You can overwrite the number, but you can't alter any specific digit by treating number as Arrau
a = 10
b = -10
c = 3.142
d = 10+3j
print('a + b = ', (a+b))
print('b + c  = ', (b+c))
print('c + d  = ', (c+d))
print('a * d  = ', (a*d))

#Convert numeric string to binary string
sstr = "10010"
snum = int(sstr, 2)
sfloat = float(sstr)
print('Binary: ', sstr, ', Int:', snum)
print('Binary: ', sstr, ', Float:', sfloat)

#Adding number at the end of the list
nums = []
nums.append(1)
#Adding number at the index
nums.insert(1, 10)
print(nums)


#Flow Control - Loops - for, while
for i in range(a):
    print('In loop: ', i*2)

#Flow Control - Conditional statements - if, else
if a>10 :
    print ('a is greater than 10')
else :
    print('a is less than or equal to 10')

#List - Ordered, changeabble, duplicable items
#Adding value at index in list
fruitList = ['Apple', 'Banana', 'Cantaloupe', 'Apple', 6, True]
print('Initialized list: ', fruitList)
print('Length of list: ', len(fruitList))
print('Type of object: ', type(fruitList))
list2 = list((1,2,3,4))
print('List initialized using constructor: ', list2)
print('Acceing items using positive index 1: ', list2[1])
print('Acceing items using negative index -1 and -2: ', list2[-1], ', ', list2[-2])
