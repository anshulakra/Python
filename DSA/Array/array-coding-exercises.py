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

def maxProduct(arr):
    max1 = 0
    max2 = 0
    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num

    return max1 * max2

l = [1,2,3,4]
print(maxProduct(l))
