# ### Missing number in Array

# def missingNumber(arr,n):
#     # finding sum of first n natural number
#     sumNno = n * (n + 1) // 2

#     # finding total sum in array
#     sumArr = sum(arr)

#     # finding missing number by subtracting sum Array from sum natural number (total)
#     answer = sumNno - sumArr

#     return answer

# l = [1,2,3,4,6]
# print(missingNumber(l,6))








###  Two Sum

# def findPairs(sum,target):
#     for i in range(len(sum)):
#         for j in range(i+1,len(sum)):
#             if sum[i] == sum[j]:
#                 continue
#             elif sum[i] + sum[j] == target:
#                 print(i,j)

# myList = [1,2,3,2,3,4,5,6]
# findPairs(myList,6)

# def two_sum(nums, target):
#     seen = {}
        
#     for i, num in enumerate(nums):
#         complement = target - num
            
#         if complement in seen:
#             return [seen[complement], i]
            
#         seen[num] = i
     
# nums = [2, 7, 11, 15]
# target = 9
# indices = two_sum(nums, target)
# print(f"Indices of the two numbers are: {indices}")








### Finding a number in Array

# import numpy as np

# def findingNumber(arr,target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1

# myArray = np.array([3,1,4,5,7,2])
# print(7 in myArray)
# print(findingNumber(myArray,7))








### Max Poduct in array

# def maxProduct(arr):
#     temp = []
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             output = arr[i] * arr[j]
#             temp.append(output)
#     print(max(temp))

# arr = [1,2,3,4]
# maxProduct(arr)

# def maxProduct(arr):
#     max1 = 0
#     max2 = 0
#     for num in arr:
#         if num > max1:
#             max2 = max1
#             max1 = num
#         elif num > max2:
#             max2 = num

#     return max1 * max2

# l = [1,2,3,4]
# print(maxProduct(l))

# l = [1,3,8,3,4]
# max0 = 0
# max1 = 0
# for i in l:
#     if i > max0:
#         max1 = max0
#         max0 = i
#     elif i > max1:
#         max1 = i
# print(max0)
# print(max1)
 






### Middle Function

# l = [1,2,3,4]
# print(l[1:-1])
# print(l[::-1])








### 2D Lists

# myList2D= [[1,2,3],[4,5,6],[7,8,9]]
# temp = 0
# for i in range(len(myList2D)):
#     print(myList2D[i][i])
#     temp += myList2D[i][i]
# print(temp)








### Best score

# myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]

# def first_second(my_list):
#     temp1 = 0
#     temp2 = 0
#     for i in my_list:
#         if i > temp1:
#             temp2 = temp1
#             temp1 = i
#         elif i > temp2:
#             temp2 = i
#     return temp1,temp2

# print(first_second(myList))








### Duplicate Number

# l = [1,1,2,3,3,2,3]

# def remove_duplicates(arr):
#     temp = []
#     for i in arr:
#         if i in temp:
#             continue
#         else:
#             temp.append(i)
#     return temp

# print(remove_duplicates(l))

# def remove_duplicates(arr):
#     temp = []
#     for i in arr:
#         if i not in temp:
#             temp.append(i)
#     return temp

# print(remove_duplicates(l))








### Pairs

# target = 7
# mylist = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]

# def pair_sum(mylist,target):
#     temp = []
#     for i in range(len(mylist)):
#         for j in range(i+1,len(mylist)):
#             if mylist[i] + mylist[j] == target:
#                 temp.append(f'{mylist[i]}+{mylist[j]}')
#     return temp

# print(pair_sum(mylist,target))








### Contains Duplicate

# l = [1,4,2,1]

# O(n2)

# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i] == l[j]:
#             print(True)

# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         print(l[i],l[j])

# O(n)

# def contain_duplicates(mylist):
#     temp = []
#     for i in mylist:
#         if i in temp:
#             return True
#         else:
#             temp.append(i)
#     return False

# print(contain_duplicates(l))







### Permutation

# def permutation(list1,list2):
#     list1.sort()
#     list2.sort()
#     if len(list1) != len(list2):
#         return False
#     elif list1 == list2:
#         return True
#     else:
#         return False
    
# list1 = [1,2,3,4]
# list2 = [2,3,1,4]

# print(permutation(list1,list2))








### Rotate Matrix/ Image

#                    Youtube                    #
