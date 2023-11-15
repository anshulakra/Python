# Average temperature calculator

days = int(input("How many day's temperature? :- "))
total = 0
tempArray = []
for i in range(days):
    temp = int(input(f"Enter day {i+1} temperature :- "))
    tempArray.append(temp)
    total = total + tempArray[i]

avg = round(total/days,2)
print(f"Average is :- {avg}")

above = 0
for i in tempArray:
    if i > above:
        above = i
if above > avg:
    print(f"Above average temperature is:- {above}")
else:
    print("All Good !")