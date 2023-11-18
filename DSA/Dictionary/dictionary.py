Creating

my_dict = dict()
print(my_dict)
print(type(my_dict))
my_dict2 = {}
print(my_dict2)
print(type(my_dict2))

eng_sp = dict(one='uno',two='dos',three='tres')
print(eng_sp)

eng_sp1 = {'one':'uno','two':'dos','three':'tres'}
print(eng_sp1)

myDict = {
    1:'Samsung',
    2:'Apple',
    3:'Nokia'
}

print(myDict)




Insert and Update

myDict = {
    'name':'Eddy',
    'age':20
}
print(myDict)
myDict['age'] = 30
print(myDict)
myDict['address'] = 'America'
print(myDict)




Travers 

myDict = {
    'name':'Eddy',
    'age':50,
    'class':10,
    'address':'Delhi'
}
print(myDict)
print(len(myDict))

for key in myDict:
    print(key,myDict[key])




Search for a element in Dictionary

Liner

myDict = {
    'name':'Eddy',
    'age':50,
    'class':10,
    'address':'Delhi'
}

def searchElement(mydict,target):
    for key in mydict:
        if mydict[key] == target:
            return key,mydict[key]
    return -1
target = 'Delhi'
print(searchElement(myDict,target))




Delete an element from Dictionary

myDict = {
    'name':'Eddy',
    'age':50,
    'class':10,
    'address':'Delhi'
}
print(myDict)
del myDict['age']
print(myDict)
myDict.pop('age')
print(myDict)
myDict.popitem()
print(myDict)
myDict.clear()
print(myDict)




Dictionary Methods

myDict = {
    'name':'Eddy',
    'age':50,
    'class':10,
    'address':'Delhi'
}

print(myDict)
myDict.clear()
print(myDict)
newDict = myDict.copy()
print(newDict)

newDict = {}.fromkeys(['name','age','class'],1)
newDict = {}.fromkeys([1,2,3,4],0)
newDict = {}.fromkeys([1,2,3,4])

print(myDict.get('age',20)) # 20 is defalut value
print(myDict.items())
print(myDict.keys())
myDict.pop('age')
print(myDict)
myDict.popitem()
print(myDict)
myDict.setdefault('name1','age')
print(myDict)
print(myDict.values())

myDict = {'name':'Sam','age':20}
newDict = {'name':'Sam','class':10}
myDict.update(newDict)
print(myDict)




Dictionary Operations

myDict = {
    1:'Samsung',
    2:'Apple',
    3:'Nokia'
}

print(1 in myDict)
print('Apple' in myDict.values())
print(len(myDict))

myDict = {
    1:'one',
    3:'three',
    2:'two'
}
print(sorted(myDict))




Dictionary comprehension
import random as r
myDict = ['paris','newyork','venic','london']
newDict = {key:r.randint(20,30) for key in myDict}
print(newDict)
print(newDict.items())
print(newDict.get('londo',0))
newDict = {key:r.randint(20,30) for key in myDict}
