# Creating an array
# import array

# my_array = array.array('i',[1,4,5,3])

# print(my_array)
# print(my_array[1])
# print(type(my_array))

# using numpy

# import numpy as np

# np_array = np.array([1,3,2],dtype=int)
# np_array = np.array([1,3,2])

# print(np_array)
# print(type(np_array))
# print(id(np_array))


####

# insertion to Array

# import array

# my_array = array.array('i',[5,3,6,3,1,7])
# print(my_array)

# my_array.insert(2,100)
# print(my_array)

# my_array.append(100)
# print(my_array)


####

# Array Traversal Operation

# import array

# myArray = array.array('i',[5,2,5,7,3,5,4,2])

# def traversArray(array):
#     for i in array:
#         print(i)

# traversArray(myArray)

####

# Accessing an element from array

# from array import *

# myArray = array('i',[1,2,3,4,5,6])

# def accessElement(array,index):
#     if index >= len(myArray):
#         print("Invalid input")
#     else:
#         print(array[index])


# accessElement(myArray,6)

####

# Searching in Array

# from array import *

# myArray = array('i',[1,2,3,4,5,6])

# # linear search

# def linearSearch(array,target):
#     for i in range(len(array)):
#         if array[i] == target:
#             return i
#     return -1

# print(linearSearch(myArray,5))


####

# Deleting an Element from array

# from array import *

# myArray = array('i',[1,2,3,4,5,6])

# myArray.pop(0)
# print(myArray)
# # remove :- it remove the element by passing it
# myArray.remove(3)
# print(myArray)