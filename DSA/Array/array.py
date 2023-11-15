####### Array

Creating an array
import array

my_array = array.array('i',[1,4,5,3])

print(my_array)
print(my_array[1])
print(type(my_array))

using numpy

import numpy as np

np_array = np.array([1,3,2],dtype=int)
np_array = np.array([1,3,2])

print(np_array)
print(type(np_array))
print(id(np_array))


###

insertion to Array

import array

my_array = array.array('i',[5,3,6,3,1,7])
print(my_array)

my_array.insert(2,100)
print(my_array)

my_array.append(100)
print(my_array)


###

Array Traversal Operation

import array

myArray = array.array('i',[5,2,5,7,3,5,4,2])

def traversArray(array):
    for i in array:
        print(i)

traversArray(myArray)

###

Accessing an element from array

from array import *

myArray = array('i',[1,2,3,4,5,6])

def accessElement(array,index):
    if index >= len(myArray):
        print("Invalid input")
    else:
        print(array[index])


accessElement(myArray,6)

###

Searching in Array

from array import *

myArray = array('i',[1,2,3,4,5,6])

# linear search

def linearSearch(array,target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

print(linearSearch(myArray,5))


###

Deleting an Element from array

from array import *

myArray = array('i',[1,2,3,4,5,6])

myArray.pop(0)
print(myArray)
# remove :- it remove the element by passing it
myArray.remove(3)
print(myArray)


# Array practice

from array import *

#1 create an Array and traverse
myArray = array('i',[1,2,3,4,5,6,6])
for i in myArray:
    print(i)

#2 Access individual elements through indexes
print(myArray[1])

#3 Append any value to the array using append() method
myArray.append(9)
print(myArray)

#4 Insert Value in an array using insert() method
myArray.insert(2,100)
print(myArray)

#5 Extend python array using extend() method
myArray1 = array('i',[7,8,9])
myArray.extend(myArray1)
print(myArray)

#6 Add item from list into array using fromlist() method
tempList = [10,11,12]
myArray.fromlist(tempList)
print(myArray)

#7 Remove any array element using remove() method
print(myArray)
myArray.remove(5)
print(myArray)

#8 Remove last array element using pop() method
myArray.pop()
print(myArray)

#9 Fetch any element through its index using index() method
print(myArray.index(6))

#10 Reverse a python array using reverse() method
myArray.reverse()
print(myArray)

#11 Get array buffer information through buffer_info() method
print(myArray.buffer_info())

#12 Check for number of occurrence of an element using count() method
print(myArray.count(6))

#13 Convert array to string using tostring() method
myArray2 = array('i',[1,22,3,4,2,4,33,5,7,6,45,19])
tempString = myArray2.tobytes()
print(tempString)

#14 Convert array to a python list with same elements using tolist() method
x = myArray2.tolist()
print(type(x))

#15 fromstring()

#16 slice elements from an array
print(myArray2[1:3])


####### 2D Array

Day 1 - 11,15,19,10
Day 2 - 22,41,31,11
Day 3 - 66,76,43,33
Day 4 - 54,32,56,83

import numpy as np

twoDArray = np.array([[11,15,19,10],[22,41,31,11],[66,76,43,33],[54,32,56,83]])
print(twoDArray)
print(twoDArray[1][1])

insertion - Two dimensional array

newTwoDArray = np.insert(twoDArray,1,[[1,2,3,4]],axis=1)
newTwoDArray = np.insert(twoDArray,1,[[1,2,3,4]],axis=0)
newTwoDArray = np.append(twoDArray,[[5,6,7,8]],axis=0)
print(newTwoDArray)

Access an element of two dimensional array

print(twoDArray[2][3])
print(len(twoDArray))
print(len(twoDArray[0]))

def accessElement(array,rowIndex,columIndex):
    if rowIndex >= len(array) or columIndex >= len(array[0]):
        print("invalid input")
    else:
        print(array[rowIndex][columIndex])

accessElement(twoDArray,4,0)
accessElement(twoDArray,1,3)


Traversal two dimensional array

twoDArray = np.array([[11,15,19,10],[22,41,31,11],[66,76,43,33],[54,32,56,83]])

for i in twoDArray:
    print(i)

def traversalTDarray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j],end=' ')
        print()

traversalTDarray(twoDArray)


Searching Two dimensional array

twoDArray = np.array([[11,15,19,10],[22,41,31,11],[66,76,43,33],[54,32,56,83]])
print(twoDArray)

def searcheElement(array,target):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == target:
                return i,j
    return -1

print(searcheElement(twoDArray,560))


Deletion in 2D array

twoDArray = np.array([[11,15,19,10],[22,41,31,11],[66,76,43,33],[54,32,56,83]])
print(twoDArray)

newtwoDArray = np.delete(twoDArray,1,axis=0)
newtwoDArray = np.delete(twoDArray,1,axis=1)

print(newtwoDArray)