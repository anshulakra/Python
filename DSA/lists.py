Lists

tempList = [1,2,3,4,[50,100],6]
print(tempList)
print(tempList[4][1])


Accessing and Traversing

tempList = ["milk","butter","bread"]
print("milk" in tempList)
print(tempList[::-1])
for i in tempList:
    print(i)

for i in range(len(tempList)):
    tempList[i] = tempList[i]+"+"
    print(tempList[i])


Update and insert a list

tempList =["milk","bread",1,"butter",9]
print(tempList)
tempList[1] = "chicken"
tempList.append("append")
tempList.insert(0,"Hi")
print(tempList)
tempList.reverse()
print(tempList)
tempList1 = ["bmw","ferarri","audi"]
tempList1.extend(tempList)
print(tempList1)


Slice and delete from list

tempList = ['a','b','c','d','e','f']
print(tempList)
print(tempList[1:3])
tempList.remove('a')
print(tempList)
tempList.pop(1)
print(tempList.pop(0))
print(tempList)
del tempList[1]
print(tempList)


Searching for an element in a List

tempList = ['nokia','samsung','mi','apple','vivo','oppo']
# in oprator
print("mi" in tempList)
liner search
def searchinElement(list,target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1
print(searchinElement(tempList,'vivo'))

def searchElement(list,target):
    for i,value in enumerate(list):
        if value == target:
            return i,value
    return -1
print(searchElement(tempList,"mi"))


List oprations and Function

tempList = [1,20,3]
tempList1 = [4,5,6]
tempList = tempList + tempList1
tempList = tempList * 3
print(tempList)
print(len(tempList))
print(max(tempList))
print(min(tempList))
print(sum(tempList))
print(sum(tempList)/len(tempList))


String and lists

s = 'String text'
s = 'String-text'

tempList = list(s)
tempList = s.split("-")
print(tempList)
print(type(tempList))


Pitfalls and ways to avoid them

tempList = [1,2,4,2,1]
tempList = tempList.sort()
print(tempList.sort())
tempList.sort()
print(tempList)


List comprehension

l = [1,2,3]
print(l)
newL = []
for i in l:
    multiL = i * 2
    newL.append(multiL)
print(newL)

l = [1,2,3]
print(l)
newL = [i for i in l]
newL = [i * 2 for i in l]
print(newL)

s = 'string'
print(s)
newL = [i for i in s]
print(newL)

With condition
l = [1,-2,4,-1,5,-7,4,-5]
print(l)
newL = [i for i in l if i >= 0]
print(newL)
